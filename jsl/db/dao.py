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

    @classmethod
    def get_article(cls):
        content = db_session.query(Article.content).filter(Article.id==1).first()
        print(content)


# CommonOper.get_article()
