from db import CommonOper, MarketInfo
import datetime

if __name__ == '__main__':
    market_info = MarketInfo()
    market_info.province = "广东"
    market_info.city = "深圳"
    CommonOper.add_one(market_info)
    d = datetime.datetime.now
    print(d)
