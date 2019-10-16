from db.dao import CommonOper
from db import db_session
from db.models import Question, People, Agree, Answer
from sqlalchemy import func, desc


def get_top_agreed_question(n):
    question_list = []
    result = db_session.query(Question.question_id, Question.title, func.count(Agree.id)).filter(
        Question.question_id == Agree.question_id, Agree.answer_id != -1).group_by(
        Question.question_id, Question.title).order_by(desc(func.count(Agree.id))).limit(n).all()
    for r in result:
        question_info = {"question_id":"", "title":"", "agree_num":""}
        question_info["question_id"], question_info["title"], question_info["agree_num"] = r
        question_list.append(question_info)
    return question_info


def get_top_agreed_answer(n):
    answer_list = []
    result = db_session.query(Answer.question_id, Answer.answer_id, func.count(Agree.id)).filter(
        Answer.question_id == Agree.question_id, Agree.answer_id == Answer.answer_id).group_by(
        Answer.question_id, Answer.answer_id).order_by(desc(func.count(Agree.id))).limit(n).all()
    for r in result:
        answer_info = {"question_id":"", "answer_id":"", "agree_num":""}
        answer_info["question_id"], answer_info["answer_id"], answer_info["agree_num"] = r
        answer_list.append(answer_info)
    return answer_list

results = get_top_agreed_answer(100)
for r in results:
    print(r)

