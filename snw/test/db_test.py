from db import CommonOper, MarketInfo, filter_redis
import datetime
import re

if __name__ == '__main__':
    name = 'snw'
    value = 'https://price.ccement.com/pricenewslist-1-440000-440404.html'
    #result = filter_redis.sadd(name, value)
    #print(result)
    #print("{}已添加".format(value))
    isExist = CommonOper.isExist(name, value)
    print("验证是否存在")
    print(isExist)
