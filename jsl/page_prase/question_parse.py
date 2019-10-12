import requests
from lxml import etree
from db.models import Question, Answer, Agree, AnswerComment
from db.dao import CommonOper
from utils import str2datetime
from tasks.workers import app
from page_prase.basic import get_html
import re

question_url_format = "https://www.jisilu.cn/question/{}"
answer_answer_url_format = "https://www.jisilu.cn/question/ajax/get_answer_answers/answer_id-{}"


def get_question_and_agree(selector):
    question = Question()
    question.question_id = selector.xpath('//div[@id="question_topic_editor"]/@data-id')[0]
    question.title = selector.xpath('//div[@class="aw-mod-head"]/h1/text()')[0]
    question.people_id = selector.xpath('//dd[@class="pull-left"]/a/@data-id')[0]
    app.send_task("tasks.people.do_people", args=(question.people_id,),
                  queue="people_queue", routing_key="people")
    post_time_str = selector.xpath('//div[@class="aw-question-detail-meta"]/div[1]/span[1]/text()')[0].replace("发表时间 ", "")
    question.post_time = str2datetime(post_time_str)
    access_time_str = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[1]/span/text()')[0]
    question.access_time = str2datetime(access_time_str)
    agree_list = selector.xpath('//div[@class="aw-question-detail-meta"]/p[contains(@class,"aw-agree-by")]/a/@data-id')
    question.read_num = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[2]/span/text()')[0]
    question.follow_num = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[3]/span/text()')[0]
    question.content = "".join(selector.xpath('//div[contains(@class,"aw-question-detail-txt")]/text()'))
    CommonOper.add_one(question)
    agrees = []
    for p in agree_list:
        app.send_task("tasks.people.do_people", args=(p,),
                      queue="people_queue", routing_key="people")
        agree = Agree()
        agree.question_id = question.question_id
        agree.people_id = p
        agrees.append(agree)
    CommonOper.add_all(agrees)


def get_answers_and_agree(selector):
    question_id = selector.xpath('//div[@id="question_topic_editor"]/@data-id')[0]
    answer_list = selector.xpath('//div[@class="aw-item"]')
    answers = []
    for a in answer_list:
        answer = Answer()
        answer.question_id = question_id
        answer.answer_id = a.xpath('@id')[0].split('_')[2]
        app.send_task("tasks.people.do_people", args=(answer.answer_id,),
                      queue="people_queue", routing_key="people")
        answer.answer_type = 1
        answer.people_id = a.xpath('a/@data-id')[0]
        answer.content = "".join(a.xpath('div/div/div[1]/div/text()'))
        post_time_str = a.xpath('div/div/div[2]/span/text()')[0]
        answer.post_time = str2datetime(post_time_str)
        answers.append(answer)
        agree_list = a.xpath('div/div/div[1]/p[2]/a/@data-id')
        answer_count_str = a.xpath('div/div/div[2]/a/text()')[0]
        #answer_count = int(answer_count_str.replace("条评论","").strip())
        answer_count = re.search('(\d+)', answer_count_str)
        if answer_count:
            app.send_task('tasks.question.do_answer_comment', args=(answer.answer_id,), queue='answer_comment_queue',
                          routing_key='answer_comment')

        agrees = []
        for p in agree_list:
            app.send_task("tasks.people.do_people", args=(p,),
                          queue="people_queue", routing_key="people")
            agree = Agree()
            agree.question_id = question_id
            agree.answer_id = answer.answer_id
            agree.people_id = p
            agrees.append(agree)
        CommonOper.add_all(agrees)
    CommonOper.add_all(answers)


def get_answer_comment(answer_id, selector):
    comment_list = selector.xpath('//ul/li')
    comment_id = 0
    answer_comments = []
    for c in comment_list:
        comment_id = comment_id + 1
        answer_comment = AnswerComment()
        answer_comment.answer_id = answer_id
        answer_comment.comment_id = comment_id
        answer_comment.people_id = c.xpath('div/a/@data-id')[0]
        app.send_task("tasks.people.do_people", args=(answer_comment.people_id,),
                      queue="people_queue", routing_key="people")
        post_time_str = c.xpath('div/span/text()')[0]
        answer_comment.post_time = str2datetime(post_time_str)
        answer_comment.content = "".join(c.xpath('div/p[@class="clearfix"]/text()'))
        answer_comments.append(answer_comment)
    CommonOper.add_all(answer_comments)


def get_relative_question(selector):
    relative_questions = selector.xpath('//ul[@class="aw-li-border-bottom"]/li')
    for question in relative_questions:
        question_id = question.xpath('a/@href')[0].split('/')[-1]
        app.send_task('tasks.question.do_question', args=(question_id,), queue='question_queue',
                      routing_key='question'
                      )


def crawl_question_and_answer(url):
    html = get_html(url)
    selector = etree.HTML(html)
    get_question_and_agree(selector)
    get_answers_and_agree(selector)
    get_relative_question(selector)


def crawl_answer_comment(url):
    html = get_html(url)
    selector = etree.HTML(html)
    answer_id = url.split('answer_id-')[1]
    get_answer_comment(answer_id, selector)


#
# url = "https://www.jisilu.cn/question/102809"
# crawl_question_and_answer(url)
# url = "https://www.jisilu.cn/question/ajax/get_answer_comments/answer_id-1288882"
# crawl_answer_comment(url)



