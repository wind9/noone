from tasks.workers import app
from page_prase import crawl_people, crawl_follows

people_url_format = "https://www.jisilu.cn/people/{}"
follows_url_format = "https://www.jisilu.cn/people/ajax/follows/type-follows__uid-{}__page-{}"


@app.task()
def do_people(people_id):
    people_url = people_url_format.format(people_id)
    crawl_people(people_url)


@app.task()
def do_follow(follower_id, page_num):
    follows_url = follows_url_format.format(follower_id, page_num)
    crawl_follows(follows_url)

