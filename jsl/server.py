from db.dao import CommonOper
from db import db_session
from db.models import Question, People, Agree, Answer, Follow
from sqlalchemy import func, desc
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", top_question=100, top_answer=100, top_follow=100)


@app.route('/top_question')
def top_question():
    questions = get_top_agreed_question(100)
    return render_template("top_question.html", questions=questions)


@app.route('/top_answer')
def top_answer():
    answers = get_top_agreed_answer(100)
    return render_template("top_answer.html", answers=answers)


@app.route('/top_follow')
def top_follow():
    follows = get_top_follow(100)
    return render_template("top_follow.html", follows=follows)


def get_top_agreed_question(n):
    question_list = []
    result = db_session.query(Question.question_id, Question.title, func.count(Agree.id)).filter(
        Question.question_id == Agree.question_id, Agree.answer_id == -1).group_by(
        Question.question_id, Question.title).order_by(desc(func.count(Agree.id))).limit(100).all()
    for r in result:
        question_info = {"question_id":"", "title":"", "agree_num":""}
        question_info["question_id"], question_info["title"], question_info["agree_num"] = r
        question_list.append(question_info)
    return question_list


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


def get_top_follow(n):
    follow_list = []
    result = db_session.query(People.people_id, People.name, func.count(Follow.id)).filter(
        Follow.refer_id == People.people_id).group_by(
        People.people_id, People.name).order_by(desc(func.count(Follow.id))).limit(n).all()
    for r in result:
        follow_info = {"name":"", "people_id":"", "follow_num":""}
        follow_info["people_id"], follow_info["name"], follow_info["follow_num"] = r
        follow_list.append(follow_info)
    return follow_list


app.run("localhost", 8080)


if __name__ == '__main__':
    questions = get_top_agreed_question(100)
    print(questions)
    for q in questions:
        #print(q)
        print("question_id:{}\ttitle:{}\tagree_num:{}".format(q['question_id'], q['title'], q['agree_num']))
