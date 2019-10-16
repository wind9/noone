import requests
from lxml import etree
from db.models import Question, Answer, Agree, AnswerComment
from db.dao import CommonOper
from utils import str2datetime
from tasks import app, task_filter
from page_prase.basic import get_html
from logger import jsl_log
import re

question_url_format = "https://www.jisilu.cn/question/{}"
answer_answer_url_format = "https://www.jisilu.cn/question/ajax/get_answer_answers/answer_id-{}"


def get_question_and_agree(question_id, selector):
    try:
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
        question.read_num = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[2]/span/text()')[0]
        question.follow_num = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[3]/span/text()')[0]
        question.content = "".join(selector.xpath('//div[contains(@class,"aw-question-detail-txt")]/text()'))
        CommonOper.add_one(question)
        CommonOper.add_filter_key("question_id", question_id)
    except Exception as e:
        jsl_log.warning("get question error,question_id:{},here are details {}".format(question_id, e))
        return
    agrees = []
    try:
        agree_list = selector.xpath('//div[@class="aw-question-detail-meta"]/p[contains(@class,"aw-agree-by")]/a/@data-id')
        for p in agree_list:
            task_filter('question', p)
            agree = Agree()
            agree.question_id = question.question_id
            agree.people_id = p
            agrees.append(agree)
        CommonOper.add_all(agrees)
    except Exception as e:
        jsl_log.warning("get agree_list error,question_id:{},here are details {}".format(question_id, e))


def get_answers_and_agree(question_id, selector):
    try:
        answer_list = selector.xpath('//div[@class="aw-item"]')
        answers = []
        for a in answer_list:
            answer = Answer()
            answer.question_id = question_id
            answer.answer_id = a.xpath('@id')[0].split('_')[2]
            task_filter('people', answer.answer_id)
            answer.answer_type = 1
            answer.people_id = a.xpath('a/@data-id')[0]
            answer.content = "".join(a.xpath('div/div/div[1]/div/text()'))
            post_time_str = a.xpath('div/div/div[2]/span/text()')[0]
            answer.post_time = str2datetime(post_time_str)
            answers.append(answer)
            answer_count_str = a.xpath('div/div/div[2]/a/text()')[0]
            answer_count = re.search('(\d+)', answer_count_str)
            if answer_count:
                app.send_task('tasks.question.do_answer_comment', args=(answer.answer_id,), queue='answer_comment_queue',
                              routing_key='answer_comment')
            agrees = []
            agree_list = a.xpath('div/div/div[1]/p[2]/a/@data-id')
            for p in agree_list:
                task_filter('people', p)
                agree = Agree()
                agree.question_id = question_id
                agree.answer_id = answer.answer_id
                agree.people_id = p
                agrees.append(agree)
            CommonOper.add_all(agrees)
        CommonOper.add_all(answers)
    except Exception as e:
        jsl_log.warning("get answer_list error,question_id:{},here are details {}".format(question_id, e))


def get_answer_comment(answer_id, selector):
    try:
        comment_list = selector.xpath('//ul/li')
        comment_id = 0
        answer_comments = []
        for c in comment_list:
            comment_id = comment_id + 1
            answer_comment = AnswerComment()
            answer_comment.answer_id = answer_id
            answer_comment.comment_id = comment_id
            answer_comment.people_id = c.xpath('div/a/@data-id')[0]
            task_filter('people', answer_comment.people_id)
            post_time_str = c.xpath('div/span/text()')[0]
            answer_comment.post_time = str2datetime(post_time_str)
            answer_comment.content = "".join(c.xpath('div/p[@class="clearfix"]/text()'))
            answer_comments.append(answer_comment)
        CommonOper.add_all(answer_comments)
    except Exception as e:
        jsl_log.warning("get answer_comment_list error,answer_id:{},here are details {}".format(answer_id, e))


def get_relative_question(question_id, selector):
    try:
        relative_questions = selector.xpath('//ul[@class="aw-li-border-bottom"]/li')
        for question in relative_questions:
            question_id = question.xpath('a/@href')[0].split('/')[-1]
            task_filter('question', question_id)
    except Exception as e:
        jsl_log.warning("get relative_question error,question_id:{},here are details {}".format(question_id, e))


def crawl_question_and_answer(url):
    html = get_html(url)
    question_id = re.findall('(\d+)', url)[0]
    if not html or ("问题不存在或已被删除" in html):
        return
    selector = etree.HTML(html)
    get_question_and_agree(question_id, selector)
    get_answers_and_agree(question_id, selector)
    get_relative_question(question_id, selector)


def crawl_answer_comment(url):
    html = get_html(url)
    if not html:
        return
    selector = etree.HTML(html)
    answer_id = url.split('answer_id-')[1]
    get_answer_comment(answer_id, selector)


#
# url = "https://www.jisilu.cn/question/320787"
# crawl_question_and_answer(url)
# url = "https://www.jisilu.cn/question/ajax/get_answer_comments/answer_id-1288882"
# crawl_answer_comment(url)



