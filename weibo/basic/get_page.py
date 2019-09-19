import requests
from config import headers, FakeChromeUA
import re
import json
import random
from logger import weibo
from exceptions import *

FAGNKE_URL = "https://passport.weibo.com/visitor/genvisitor"
extract_pattern = "({.*})"
brower_type, brower_version = FakeChromeUA.brower_version.split('/')
brower_info = "".join([brower_type,",".join(brower_version.split('.'))])


def get_tid_and_cw():
    fp = "{" + '"os":"1","browser":"{}","fonts":"undefined","screenInfo":"1920*1080*24","plugins":' \
    '"Portable Document Format::internal-pdf-viewer::Chrome PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF Viewer|::internal-nacl-plugin::Native' \
    ' Client"'.format(brower_info)+'}'
    post_data = {
        "cb": "gen_callback",
        "fp": fp
    }
    try:
        resp = requests.post(FAGNKE_URL, data=post_data, headers=headers)
        content = resp.content.decode('utf-8')
        print(content)
        m = re.search(extract_pattern, content)
        gen_visitor = json.loads(m.group())
        tid = gen_visitor.get("data").get("tid")
        new_tid = gen_visitor.get("new_tid")
        confidence = gen_visitor.get("data").get("confidence", 100)
        if confidence< 100:
            confidence = '0' + str(confidence)
        if str(new_tid).lower() == 'false':
            w = 2
        else:
            w = 3
        return tid, confidence, w
    except AttributeError:
        raise CookieGenException("failed to gen login without login")

@retry(10,1,CookieGenException)
def get_cookies():
    fetch_cookies_url = "https://passport.weibo.com/visitor/visitor"
    tid, confidence, w = get_tid_and_cw()
    post_data = {
        "a": "incarnate",
        "t": tid,
        "w": w,
        "c": confidence,
        "gc": "",
        "cb": "cross_domain",
        "from": "weibo",
        "_rand": format(random.random(),'.17f')
    }
    print(post_data)
    resp = requests.get(fetch_cookies_url, params=post_data)
    html = resp.content.decode('utf-8')
    pattern = "({.*})"
    m = re.search(pattern, html)
    json_data = json.loads(m.group())
    sub = json_data.get("data").get("sub")
    subp = json_data.get("data").get("subp")
    return dict(SUB=sub, SUBP=subp)

if __name__ == '__main__':
    tid, confidence = get_cookies()
    print(tid, confidence)
