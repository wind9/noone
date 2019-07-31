from .basic import db_session
from .models import StockInfo, StorkDayPrice
from decorators import db_commit_decorator
from sqlalchemy.exc import IntegrityError as SqlalchemyIntegrityError
from sqlalchemy.exc import InvalidRequestError
from pymysql.err import IntegrityError as PymysqlIntegrityError


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
        except (SqlalchemyIntegrityError, PymysqlIntegrityError, InvalidRequestError):
            for data in datas:
                cls.add_one(data)


class StockInfoOper:
    @classmethod
    @db_commit_decorator
    def insert_stock_info(cls, coop_code, coop_name, stock_code, stock_name, reg_date, total_share, circulating_share,
                          industry, security_type, market):
        stock_info = StockInfo()
        stock_info.coop_code = coop_code
        stock_info.coop_name = coop_name
        stock_info.stock_code = stock_code
        stock_info.stock_name = stock_name
        stock_info.reg_date = reg_date
        stock_info.total_share = total_share
        stock_info.circulating_share = circulating_share
        stock_info.industry = industry
        stock_info.security_type = security_type
        stock_info.market = market
        db_session.add(stock_info)
        db_session.commit()

    @classmethod
    def get_stock_info(cls):
        return db_session.query(StockInfo).all()


class StockDayPriceOper:
    @classmethod
    @db_commit_decorator
    def insert_day_price(cls, stock_code, trade_date, open, high, close, low, chg, percent, volume, lot_volume):
        stock_day_price = StorkDayPrice()
        stock_day_price.stock_code = stock_code
        stock_day_price.trade_date = trade_date
        stock_day_price.open = open
        stock_day_price.high = high
        stock_day_price.close = close
        stock_day_price.low = low
        stock_day_price.chg = chg
        stock_day_price.percent = percent
        stock_day_price.volume = volume
        stock_day_price.lot_volume = lot_volume
        db_session.add(stock_day_price)
        db_session.commit()


