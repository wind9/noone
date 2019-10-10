from tasks.workers import app
from page_prase import crawl_people

people_url_format = "https://www.jisilu.cn/people/{}"


@app.task()
def do_people(people_id):
    people_url = people_url_format.format(people_id)
    crawl_people(people_url)
