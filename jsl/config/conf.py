from yaml import load
import os

config_file_path = os.path.join(os.path.dirname(__file__), 'jsl.yaml')

with open(config_file_path, 'r') as f:
    content = f.read()

cf = load(content)


def get_mysql_args():
    return cf.get('mysql')


def get_redis_args():
    return cf.get('redis')


if __name__ == '__main__':
    mysql_args = get_mysql_args()
    print(mysql_args)
