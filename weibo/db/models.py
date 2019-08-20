from .tables import *
from .basic import Base


class LoginInfo(Base):
    __table__ = login_info


class User(Base):
    __table__ = wbuser

    def __init__(self, uid):
        self.uid = uid

