from .tables import stock_info
from .basic import Base


class StockInfo(Base):
    __table__ = stock_info

