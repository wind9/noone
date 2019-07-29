from yaml import load
import os

config_path = os.path.join(os.path.dirname(__file__), 'stock.yaml')

with open(config_path) as f:
    content = f.read()

cf = load(content)


def get_db_args():
    return cf.get('db')