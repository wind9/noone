from db.models import *
from db.basic import db_session


class CommonOper:
    @classmethod
    def add_one(cls, data):
        db_session.add(data)
        db_session.commit()

    @classmethod
    def add_all(cls, datas):
        try:
            db_session.add_all(datas)
            db_session.commit()
        except Exception:
            for data in datas:
                cls.add_one(data)


class QuestionOper:
    @classmethod
    def is_exist(cls, question_id):
        count = db_session.query(Question.question_id).filter(Question.question_id == question_id).count()
        if count:
            return True
        else:
            return False


class PeopleOper:
    @classmethod
    def is_exist(cls, people_id):
        count = db_session.query(People.people_id).filter(People.people_id == people_id).count()
        if count:
            return True
        else:
            return False


# question_id = 102809
# QuestionOper.is_exist(question_id)
