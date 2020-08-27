from db import market_info, Base


class MarketInfo(Base):
    __table__ = market_info

    def __repr__(self):
        return "{}{}{}日{}价格：{}".format(self.province, self.city, self.price_date, self.brand, self.price)
