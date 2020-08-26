from db import db_session


class CommonOper:
    @classmethod
    def add_one(self, data):
        db_session.add(data)
        db_session.commit()

    @classmethod
    def add_all(self, datas):
        try:
            db_session.add_all(datas)
        except Exception:
            for data in datas:
                self.add_one(data)
