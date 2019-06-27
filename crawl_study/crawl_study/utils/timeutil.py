# coding: utf-8
import datetime, time


def now_time():
    return datetime.datetime.now()


def this_day():
    return now_time().strftime('%Y%m%d')


def yes_time():
    return now_time() + datetime.timedelta(days=-1)


def yes_day():
    return yes_time().strftime('%Y%m%d')


def utc13():
    return str(int(round(time.time()*1000)))


if __name__ == '__main__':
    utc13 = utc13()
    print(utc13)
