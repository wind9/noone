import time
from datetime import datetime


def get_utc13():
    return str(int(time.time()*1000))

__all__ = ['get_utc13']

if __name__ == '__main__':
    utc13 = get_utc13()
    print(utc13)