import base64
from builtins import object
from urllib.parse import quote_plus
import binascii
import requests
import rsa
from config import headers, get_code_username, get_code_password
from exceptions import LoginException
from utils import getIP, get_utc13
import os


YUNDAMA_USERNAME = os.getenv('YUNDAMA_ACCOUNT') or get_code_username()
YUNDAMA_PASSWORD = os.getenv('YUNDAMA_PASSWORD') or get_code_password()


def get_encodename(username):
    username_quote = quote_plus(str(username))
    username_base64 = base64.b64encode(username_quote.encode('utf-8'))
    return username_base64.decode('utf-8')


def get_server_data(su, session, proxy):
    pre_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su="
    prelogin_url = "{}{}&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_={}".format(pre_url, su, get_utc13())
    pre_data_resp = session.get(prelogin_url, proxies=proxy, headers=headers)
    server_data = eval(pre_data_resp.content.decode('utf-8').replace("sinaSSOController.preloginCallBack", ""))
    return server_data


def get_password(password, servertime, nonce, pubkey):
    ras_publickey = int(pubkey, 16)
    key = rsa.PublicKey(ras_publickey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    message = message.encode('utf-8')
    passwd = rsa.encrypt(message, key)
    passwd = binascii.b2a_hex(passwd)
    return passwd


def login_by_pincode(username, password, session, server_data, retry_count, proxy):
    post_url = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)"
    servertime = server_data["servertime"]
    nonce = server_data["nonce"]
    rsakv = server_data["rsakv"]
    pubkey = server_data['pubkey']
    pcid = server_data['pcid']
    sp = get_password(password, servertime, nonce, pubkey)
    data = {
        'encoding': 'UTF-8',
        'entry': 'weibo',
        'from': '',
        'gateway': '1',
        'nonce': nonce,
        'pagerefer': "",
        'prelt': 67,
        'pwencode': 'rsa2',
        "returntype": "META",
        'rsakv': rsakv,
        'savestate': '7',
        'servertime': servertime,
        'service': 'miniblog',
        'sp': sp,
        'sr': '1920*1080',
        'su': get_encodename(username),
        'useticket': '1',
        'vsnf': '1',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'pcid': pcid
    }
    if not YUNDAMA_USERNAME:
        raise LoginException('Login need verfication code, please set your yundama info in config/spider.yaml')
    img_url = get_pincode_url(pcid)
    return rs, yundama_obj, cid, session



def login_no_pincode(username, password, session, server_data, proxy):
    pass


def do_login(username, password, proxy):
    session = requests.Session()
    su = get_encodename(username)
    server_data = get_server_data(su, session, proxy)
    if server_data['showpin']:
        rs, yundama_obj, cid, session = login_by_pincode(username, password, session, server_data, 0, proxy)
    else:
        rs, yundama_obj, cid, session = login_no_pincode(username, password, session, server_data, 0, proxy)

def get_session(username, password):
    proxy = getIP("")
    url, yundama_obj, cid, session = do_login(username, password, proxy)


if __name__ == '__main__':
    username = 'lierkui_123@163.com'
    password = '890820wb'
    get_session(username, password)

