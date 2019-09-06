from lxml import etree
import requests
import re
import json


def get_follows_fans_tweets(html):
    pattern = "FM.view\((.*)\)"
    m = re.findall(pattern, html)
    for g in m:
        if "Pl_Core_T8CustomTriColumn__3" in g and "WB_innerwrap" in g:
            jdata = json.loads(g)
            user_info_html = jdata.get('html')
            break
    selector = etree.HTML(user_info_html)
    follows = selector.xpath('/html/body/div/div/div/table/tbody/tr/td[1]/a/strong/text()')[0]
    fans = selector.xpath('/html/body/div/div/div/table/tbody/tr/td[2]/a/strong/text()')[0]
    tweets = selector.xpath('/html/body/div/div/div/table/tbody/tr/td[3]/a/strong/text()')[0]
    return follows, fans, tweets



def test(html):
    selector = etree.HTML(html)
    id = selector.xpath('/html/body/div[1]/div[21]/span[1]/a[4]/text()')
    return id


if __name__ == '__main__':
    test_url = "https://www.qq.com/"
    r = requests.get(test_url)
    id = test(r.text)
    print(id)