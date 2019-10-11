from page_prase.headers import user_agents
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
    html = requests.get(url, proxies=proxies, headers=headers).content
    if isinstance(html, bytes):
        html = html.decode("utf-8")
    return html
