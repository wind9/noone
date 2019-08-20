from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from config import get_db_args


def get_engine():
    db_args = get_db_args()
    password = os.getenv('DB_PASS', db_args['password'])
    connect_str = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(db_args['db_type'], db_args['db_connect_type'], db_args['user'], password,
                                                                  db_args['host'], db_args['port'], db_args['db_name'])
    engine = create_engine(connect_str)
    return engine


eng = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=eng)
db_session = Session()
metadata = MetaData(get_engine())


__all__ = ['eng', 'Base', 'db_session', 'metadata']

