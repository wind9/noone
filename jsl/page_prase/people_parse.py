import requests
from lxml import etree
from db.models import People
import re


def get_people_and_follow(people_id, selector):
    people = People()
    people.id = people_id
    people.people_name = selector.xpath('//div[@class="aw-user-center"]/div/h1/text()')[0]
    people.people_desc = "".join(selector.xpath('//div[@class="aw-user-center"]/div/span/text()'))
    people_locate_spans = selector.xpath('//div[@class="aw-user-center"]/div/p[3]/span')
    if len(people_locate_spans) == 4:
        people.province = people_locate_spans[1].xpath('a[1]/@href')
        people.city = people_locate_spans[1].xpath('a[2]/@href')
        people.sex = people_locate_spans[2].xpath('text()')[0]
        home_access_str = people_locate_spans[3].xpath('text()')[0]
        people.home_access_num = re.match('\d+', home_access_str)
    else:
        home_access_str = people_locate_spans[1].xpath('text()')[0]
        people.home_access_num = re.match('\d+', home_access_str)
    people_type_spans = selector.xpath('//div[@class="aw-user-center"]/div/p[4]/span')
    people.people_type = people_type_spans[0].xpath('a/em/text()')[0]
    people.weiwang_num = people_type_spans[1].xpath('em/text()')[0]
    people.agree_num = people_type_spans[2].xpath('em/text()')[0]
    people.thanks_num = people_type_spans[3].xpath('em/text()')[0]
    people.gold_num = people_type_spans[4].xpath('em/text()')[0]


def crawl_people(url):
    html = requests.get(url).content
    selector = etree.HTML(html)
    people_id = url.split('/')[-1]
    get_people_and_follow(people_id, selector)


# url = "https://www.jisilu.cn/people/102809"
# crawl_people(url)




