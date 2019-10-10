from tasks.workers import app
from page_prase import crawl_question_and_answer, crawl_answer_comment
from db.dao import QuestionOper

question_url_format = "https://www.jisilu.cn/question/{}"
answer_comment_url_format = "https://www.jisilu.cn/question/ajax/get_answer_comments/answer_id-{}"


@app.task()
def do_question(question_id):
    if not QuestionOper.is_exist(question_id):
        question_url = question_url_format.format(question_id)
        crawl_question_and_answer(question_url)
    else:
        print("question id:{}已存在，跳过".format(question_id))


@app.task()
def do_answer_comment(comment_id):
    answer_comment_url = answer_comment_url_format.format(comment_id)
    crawl_answer_comment(answer_comment_url)


