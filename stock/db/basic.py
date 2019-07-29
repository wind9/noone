from sqlalchemy import create_engine , MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_db_args


def get_engine():
    db_args = get_db_args()
    connect_str = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(db_args['db_type'], db_args['connect_type'],
                                                  db_args['user'], db_args['pass'], db_args['host'], db_args['port'], db_args['db_name'])
    engine = create_engine(connect_str, encoding='utf-8')
    return engine


engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()
metadata = MetaData(engine)

__all__ = ['engine', 'Base', 'db_session', 'metadata']


