from .models import LoginInfo
from .basic import db_session
from sqlalchemy import text


class LoginInfoOper:
    @classmethod
    def get_login_info(cls):
        return db_session.query(LoginInfo.name, LoginInfo.password, LoginInfo.enable).filter(text('enable=1')).all()
