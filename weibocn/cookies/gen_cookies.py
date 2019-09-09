import requests
from config import headers
import random
import re
import json
from page_parse import get_follows_fans_tweets

GENVISTOR_URL1 = "https://passport.weibo.com/visitor/genvisitor"
GENVISTOR_URL2 = "https://passport.weibo.com/visitor/visitor"


def get_tid_c_w():
    fp = {"os":"1","browser":"Chrome76,0,3809,132","fonts":"undefined","screenInfo":"1920*1080*24","plugins":"Portable Document Format::internal-pdf-viewer::Chrome PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF Viewer|::internal-nacl-plugin::Native Client"}
    post_data = {
        "cb": "gen_callback",
        "fp": fp
    }
    r = requests.post(GENVISTOR_URL1, headers=headers, data=post_data)
    pattern = "({.*})"
    m = re.search(pattern, r.text)
    s = m.group()
    jdata = json.loads(s)
    tid = jdata.get('data').get('tid')
    return tid, '095', 2


def get_cookies():
    tid, c, w = get_tid_c_w()
    post_data = {
        "a": "incarnate",
        "t": tid,
        "w": 2,
        "c": c,
        "gc": "",
        "cb": "cross_domain",
        "from": "weibo",
        "_rand": format(random.random(), '.17f')
    }
    r = requests.get(GENVISTOR_URL2, params=post_data, headers=headers)
    pattern = "({.*})"
    m = re.search(pattern, r.text)
    s = m.group()
    jdata = json.loads(s)
    sub = jdata.get('data').get('sub')
    subp = jdata.get('data').get('subp')
    return dict(SUB=sub,SUBP=subp)


cookies = get_cookies()
test_url = "https://weibo.com/hanhan"
r = requests.get(test_url, cookies=cookies, headers=headers)
#print(r.text)
follows, fans, tweets = get_follows_fans_tweets(r.text)
print(follows, fans, tweets)