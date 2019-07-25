from functools import wraps
from logger import storage
from db.basic import db_session


def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            storage.error("DB operation error, here are details:{}".format(e))
            db_session.rollback()
        return session_commit

