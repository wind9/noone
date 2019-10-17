from page_prase.headers import user_agents
from logger import jsl_log
import random
import requests


def get_html(url):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    proxies = {
        "http": "http://{}:{}@http-dyn.abuyun.com:9020".format("HVR27NV2EN90868D", "48A8F2CA4229A4F9"),
        "https": "http://{}:{}@http-dyn.abuyun.com:9020".format("HVR27NV2EN90868D", "48A8F2CA4229A4F9")
    }
    html = ''
    try:
        r = requests.get(url, proxies=proxies, headers=headers, allow_redirects=True)
        html = r.content
        if isinstance(html, bytes):
            html = html.decode("utf-8")
    except Exception as e:
        jsl_log.warning("get templates error,url:{},here are details {}".format(url, e))
    finally:
        return html
