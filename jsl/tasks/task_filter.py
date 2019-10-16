from db.dao import CommonOper
from tasks.workers import app
from logger import jsl_log


def task_filter(task_type, param):
    if task_type == 'question':
        if not CommonOper.is_exist("question_id", param):
            app.send_task('tasks.question.do_question', args=(param,), queue='question_queue',
                          routing_key='question'
                          )
        else:
            jsl_log.info("相关question已存在,question_id:".format(param))
    elif task_type == 'people':
        if not CommonOper.is_exist("people_id", param):
            app.send_task('tasks.question.do_people', args=(param,), queue='people_queue',
                          routing_key='people'
                          )
        else:
            jsl_log.info("相关people已存在,people_id:".format(param))
