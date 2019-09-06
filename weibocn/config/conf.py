from yaml import load
import os

config_file_path = os.path.join(os.path.dirname(__file__), 'weibo.cn.yaml')
with open(config_file_path,'r') as f:
    content = f.read()
cf = load(content)


def get_db_args():
    return cf.get('db')


__all__ = ['get_db_args']