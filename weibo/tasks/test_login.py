#from .workers import app
#from db.dao import LoginInfoOper
import requests
from urllib.parse import urlencode
import json
from utils import get_utc13


#@app.task(ignore_result=True)
#def execute_login_task():
#   infos = LoginInfoOper.get_login_info()


def pre_login(session):
    pre_url1 = "https://passport.weibo.cn/sso/login"
    pre_data1 = {
        "username": "lierkui_123@163.com",
        "password": "890820wb",
        "savestate": "1",
        "r": "https://weibo.cn/",
        "ec": "0",
        "pagerefer": "https://weibo.cn/pub/",
        "entry": "mweibo",
        "wentry": "",
        "loginfrom": "",
        "client_id": "",
        "code": "",
        "qq": "",
        "mainpageflag": "1",
        "hff": "",
        "hfp": ""
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
    }
    #req = requests.get(url, proxies = proxy, verify=False)
    req = session.post(pre_url1, data=pre_data1, proxies=None, headers=headers)
    print(req.status_code)
    html = req.content.decode('utf-8')
    print(html)
    jdata = json.loads(html)
    print(jdata)
    return session, jdata


def pre_login1(session, jdata):
    timestamp = get_utc13()
    if jdata['retcode']  == 20000000:
        pre_url2 = "{}&savestate=1&callback=jsonpcallback{}".format(jdata['data']['crossdomainlist']['sina.com.cn'], timestamp)
    print(pre_url2)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
    }
    #req = requests.get(url, proxies = proxy, verify=False)
    req = session.get(pre_url2, proxies=None, headers=headers)
    print(req.status_code)
    html = req.content.decode('utf-8')
    print(html)
    return session, jdata


def pre_login2(session, jdata):
    timestamp = get_utc13()
    if jdata['retcode']  == 20000000:
        pre_url2 = "{}&savestate=1&callback=jsonpcallback{}".format(jdata['data']['crossdomainlist']['weibo.com'], timestamp)
    print(pre_url2)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
    }
    #req = requests.get(url, proxies = proxy, verify=False)
    req = session.get(pre_url2, proxies=None, headers=headers)
    print(req.status_code)
    html = req.content.decode('utf-8')
    print(html)
    return session, jdata


def pre_login3(session, jdata):
    timestamp = get_utc13()
    if jdata['retcode']  == 20000000:
        pre_url2 = "{}&savestate=1&callback=jsonpcallback{}".format(jdata['data']['crossdomainlist']['weibo.cn'], timestamp)
    print(pre_url2)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
    }
    #req = requests.get(url, proxies = proxy, verify=False)
    req = session.get(pre_url2, proxies=None, headers=headers)
    print(req.status_code)
    html = req.content.decode('utf-8')
    print(html)
    return session, jdata


def get_home_page(session):
    home_url = "https://weibo.cn/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
    }
    req = session.get(home_url, proxies=None, headers=headers)
    print(req.text)


if __name__ == '__main__':
    session = requests.Session()
    session , jdata = pre_login(session)
    cookies = session.cookies.get_dict()
    print(cookies)
    # print("--------------prelogin1----------")
    # session1, jdata1 = pre_login1(session, jdata)
    # cookies1 = session1.cookies
    # print(cookies1)
    # print("--------------prelogin2----------")
    # session2, jdata2 = pre_login1(session1, jdata)
    # cookies2 = session2.cookies
    # print(cookies2)
    # print("--------------prelogin3----------")
    # session3, jdata3 = pre_login1(session2, jdata)
    # cookies3 = session2.cookies
    # print(cookies3)
    print('-------------------home page----------')
    get_home_page(session)
