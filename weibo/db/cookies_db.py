import redis
from config import get_redis_args

redis_args = get_redis_args()
host = redis_args.get('host','127.0.0.2')
port = redis_args.get('port',6379)
password = redis_args.get('password','')
cookies_db = redis_args.get('login', 3)
broker_db = redis_args.get('login', 1)

cookies_con = redis.Redis(host=host,port=port,password=password,db=cookies_db)
broker_con = redis.Redis(host=host,port=port,password=password,db=broker_db)


class Cookies(object):
    @classmethod
    def check_login_task(cls):
        if broker_con.llen('login_queue') > 0:
            broker_con.delete('login_queue')

