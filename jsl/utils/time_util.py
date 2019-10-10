import datetime


def str2datetime(time_str):
    return datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M')

