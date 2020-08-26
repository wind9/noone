from yaml import load
import os


config_path = os.path.join(os.path.dirname(__file__), 'snw.yaml')

with open(config_path, 'r') as f:
    content = f.read()
cf = load(content)


def get_redis_args():
    return cf.get('redis')


def get_mysql_args():
    return cf.get('mysql')


# redis_args = get_redis_args()
# print(redis_args)