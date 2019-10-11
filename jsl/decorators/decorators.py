from functools import wraps
from db.basic import db_session
from logger import jsl_log


def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            jsl_log.info("DB operation error,here are details :{}".format(e))
            db_session.rollback()
    return session_commit
