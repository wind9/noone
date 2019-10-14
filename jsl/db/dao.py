from db.models import *
from db.basic import db_session, filter_redis
from decorators import db_commit_decorator
from config import get_redis_args


class CommonOper:
    @classmethod
    @db_commit_decorator
    def add_one(cls, data):
        db_session.add(data)
        db_session.commit()

    @classmethod
    @db_commit_decorator
    def add_all(cls, datas):
        try:
            db_session.add_all(datas)
            db_session.commit()
        except Exception:
            for data in datas:
                cls.add_one(data)

    @classmethod
    def is_exist(cls, key_type, key):
        is_exist = filter_redis.sismember(key_type, key)
        return is_exist

    @classmethod
    def add_filter_key(cls, key_type, key):
        filter_redis.sadd(key_type, key)


# key_type = 'kk'
# check_id = '88488'
# result = CommonOper.is_exist(key_type, check_id)
# print(result)