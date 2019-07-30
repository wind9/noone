from .tables import stock_info, stock_day_price
from .basic import Base


class StockInfo(Base):
    __table__ = stock_info


class StorkDayPrice(Base):
    __table__ = stock_day_price

