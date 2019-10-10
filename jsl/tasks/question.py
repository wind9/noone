from worker import app
from lxml import etree
from page_prase.question_parse import crawl_question_and_answer, crawl_answer_comment
import requests

article_url_format = "https://www.jisilu.cn/question/{}"
answer_comment_url_format = "https://www.jisilu.cn/question/ajax/get_answer_comments/answer_id-{}"


@app.task()
def do_question(article_id):
    article_url = article_url_format.format(article_id)
    crawl_question_and_answer(article_url)


@app.task()
def do_answer_comment(comment_id):
    answer_comment_url = article_url_format.format(comment_id)
    crawl_answer_comment(answer_comment_url)


