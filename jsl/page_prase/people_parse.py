from lxml import etree
from db.models import People, Follow
from utils import str2datetime
from page_prase.basic import get_html
from tasks.workers import app
from db.dao import CommonOper
import re


def get_people_and_follows(people_id, selector):
    people = People()
    people.people_id = people_id
    people.name = selector.xpath('//div[@class="aw-user-center"]/div[1]/div/h1/text()')[0].strip()
    people.desc = "".join(selector.xpath('//div[@class="aw-user-center"]/div[1]/div/span/text()'))
    if selector.xpath('//i[contains(@class,"i-user-locate")]'):
        user_locate = selector.xpath('//i[contains(@class,"i-user-locate")]')[0].getparent()
        people.province = user_locate.xpath('a[1]/text()')[0]
        people.city = user_locate.xpath('a[2]/text()')[0]
    if selector.xpath('//i[contains(@class,"i-user-post")]'):
        user_post = selector.xpath('//i[contains(@class,"i-user-post")]')[0].getparent()
        people.post = "".join(user_post.xpath('text()')).strip()
    if selector.xpath('//i[contains(@class,"i-user-visits")]'):
        user_visits = selector.xpath('//i[contains(@class,"i-user-visits")]')[0].getparent()
        user_visits_str = "".join(user_visits.xpath('text()'))
        people.home_visit_num = re.findall('(\d+)', user_visits_str)[0]
    people_type_spans = selector.xpath('//div[@class="aw-user-center"]/div[1]/div/p[3]/span')
    people.user_type = people_type_spans[0].xpath('a/em/text()')[0].replace("»","").strip()
    people.weiwang_num = people_type_spans[1].xpath('em/text()')[0]
    people.agree_num = people_type_spans[2].xpath('em/text()')[0]
    people.thanks_num = people_type_spans[3].xpath('em/text()')[0]
    people.gold_num = people_type_spans[4].xpath('em/text()')[0]
    if '+' in people.gold_num:
        people.gold_num = 100
    if len(selector.xpath('//dd')) > 1:
        last_active_time_str = selector.xpath('//div[@id="detail"]/div/dl[2]/dd/text()')[0]
        people.last_active_time = str2datetime(last_active_time_str)
    CommonOper.add_one(people)
    app.send_task("tasks.people.do_follow", args=(people_id, 0,), queue="people_queue", routing_key="people")


def get_follows(follower_id, page_num, selector):
    follow_list = selector.xpath('//li')
    follows = []
    if len(follow_list) == 30:
        app.send_task("tasks.people.do_follow", args=(follower_id, int(page_num)+1,),
                      queue="people_queue", routing_key="people")
    for f in follow_list:
        follow = Follow()
        follow.refer_id = f.xpath('div/a/@data-id')[0]
        follow.follow_type = 1
        follow.follower_id = follower_id
        follows.append(follow)
    CommonOper.add_all(follows)


def crawl_people(url):
    html = get_html(url)
    selector = etree.HTML(html)
    people_id = url.split('/')[-1]
    get_people_and_follows(people_id, selector)


def crawl_follows(url):
    html = get_html(url)
    if not html:
        return
    selector = etree.HTML(html)
    follower_id = re.findall("uid-(\d+)", url)[0]
    page_num = re.findall("page-(\d+)", url)[0]
    get_follows(follower_id, page_num, selector)


if __name__ == '__main__':
    # url = "https://www.jisilu.cn/people/ajax/follows/type-follows__uid-323339__page-0"
    # crawl_follows(url)
    url = "https://www.jisilu.cn/people/88918"
    crawl_people(url)




