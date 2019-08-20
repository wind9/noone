from yaml import load
import os

config_file_path = os.path.join(os.path.dirname(__file__),'weibo.yaml')
with open(config_file_path) as f:
    content = f.read()
cf = load(content)


def get_redis_args():
    return cf.get('redis')


def get_redis_master():
    return cf.get('master', '')

def get_db_args():
    return cf.get('db')


def get_broker_and_backend():
    redis_info = cf.get('redis')
    password = redis_info.get('pass')
    sentinel_args = redis_info.get('sentinel')
    db = redis_info.get('broker', 5)
    if sentinel_args:
        broker_url = ";".join('sentinel://:{}@{}:{}/{}'.format(password, sentinel['host'], sentinel['port'], db) for sentinel in sentinel_args)
        return broker_url
    else:
        host = redis_info.get('host')
        port = redis_info.get('port')
        backend_db = redis_info.get('backend', 6)
        broker_url = 'redis://{}@{}:{}/{}'.format(password, host, port, db)
        backend_url = 'redis://{}@{}:{}/{}'.format(password, host, port, backend_db)
        return broker_url, backend_url


__all__ = ['get_redis_args', 'get_db_args', 'get_broker_and_backend', 'get_redis_master']


if __name__ == '__main__':
    broker_and_backend = get_broker_and_backend()
    if isinstance(broker_and_backend, tuple):
        broker_url, backend_url  = broker_and_backend
        print(broker_url, backend_url)
    else:
        broker_url = broker_and_backend
        print(broker_url)

