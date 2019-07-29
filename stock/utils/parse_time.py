import time
from datetime import datetime


def get_timestamp():
    return int(time.time()*1000)


def date2timstamp(format_date):
    ts = time.strptime(format_date,"%Y%m%d")
    print(ts)
    print(datetime.now())
    timestamp = time.mktime(ts)*1000
    return timestamp

def utc2local( utc_dtm ):
    # UTC 时间转本地时间（ +8:00 ）
    local_tm = datetime.fromtimestamp( 0 )
    utc_tm = datetime.utcfromtimestamp( 0 )
    offset = local_tm - utc_tm
    return utc_dtm + offset

def local2utc( local_dtm ):
    # 本地时间转 UTC 时间（ -8:00 ）
    return datetime.utcfromtimestamp( local_dtm.timestamp() )




if __name__ == '__main__':
    timestamp = get_timestamp()
    print(timestamp)
    format_date = '19961118'
    timestamp = date2timstamp(format_date)
    print(timestamp)
    print(type(timestamp))
    utc_time = datetime.utcnow()
    print(utc_time)
    src_time = utc_time.strftime("%Y-%m-%d %H:%M:%S")
    print(src_time)