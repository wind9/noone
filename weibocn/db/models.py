from .basic import Base
from .tables import *


class UserInfo(Base):
    __table__ = wb_user_info
