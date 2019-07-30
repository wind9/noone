import time
from datetime import datetime


def get_now_str():
    d = datetime.now()
    print(d)
    print(type(d))
    d2 = datetime.strftime(d,'%Y%m%d%H%M%S')
    print(d2)
    return int(time.time()*1000)


def date2timstamp(format_date):
    ts = time.strptime(format_date + '000000',"%Y%m%d%H%M%S")
    timestamp = int(time.mktime(ts)*1000)
    return timestamp


def timestamp2date(timestamp):
    localtime = time.localtime(timestamp)
    date = time.strftime('%Y%m%d', localtime)
    return date


def get_now_timestamp():
    return str(int(time.time()*1000))


if __name__ == '__main__':
    s = get_now_str()
    print(s)
    s2 = date2timstamp('20190211')
    print(s2)
    s3 = timestamp2date(848246400000/1000)
    print(s3)

