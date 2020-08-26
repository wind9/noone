from db import CommonOper, MarketInfo
import datetime
import re

if __name__ == '__main__':
    s = "来源：水泥网信息中心      发布日期：2020-08-26 17:13:53"
    p = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
    r = re.findall(p, s)
    print(r)
