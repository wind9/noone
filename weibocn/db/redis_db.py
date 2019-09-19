import redis
from config import get_redis_args


redis_args = get_redis_args()
cookies_con = redis.Connection(host=redis_args.get('host'), port=redis_args.get('port'),
                               password=redis_args.get('password'), db=redis_args.get('cookies_db'))


class Cookies:
    @classmethod
    def store_cookies(cls, json_str):
        cookies_con.lpush("login", json_str)


