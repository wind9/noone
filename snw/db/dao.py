from db import db_session, filter_redis


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
    def isExist(cls, name, value):
        return filter_redis.sismember(name, value)

    @classmethod
    def add_filter_key(cls, name, value):
        filter_redis.sadd(name, value)

