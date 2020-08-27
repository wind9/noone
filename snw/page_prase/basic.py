import requests
import random
from page_prase.headers import user_agents
from logger import log
from lxml import etree


base_url = "https://price.ccement.com"


def get_html(url):
    html = ''
    user_agent = random.choice(user_agents)
    header = {
        "User-Agent": user_agent
    }
    try:
        r = requests.get(url, headers=header)
        resp = r.content
        if isinstance(resp, bytes):
            html = resp.decode('utf-8')
    except Exception as e:
        log.info("请求页面执行异常,页面url:{}".format(url))
        log.exception(e)
    finally:
        return html


def get_selector(url):
    selector = None
    html = get_html(url)
    #print(html)
    if html:
        selector = etree.HTML(html)
    return selector
