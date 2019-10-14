from tasks.workers import app
from page_prase import crawl_people, crawl_follows
from db.dao import CommonOper
from logger import jsl_log

people_url_format = "https://www.jisilu.cn/people/{}"
follows_url_format = "https://www.jisilu.cn/people/ajax/follows/type-follows__uid-{}__page-{}"


@app.task()
def do_people(people_id):
    if not CommonOper.is_exist("people_id", people_id):
        people_url = people_url_format.format(people_id)
        jsl_log.info("开始爬取url:{}".format(people_url))
        crawl_people(people_url)
    else:
        jsl_log.info("people id:{}已存在，跳过".format(people_id))


@app.task()
def do_follow(follower_id, page_num):
    follows_url = follows_url_format.format(follower_id, page_num)
    jsl_log.info("开始爬取url:{}".format(follows_url))
    crawl_follows(follows_url)

