from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_db_args


def get_engine():
    db_args = get_db_args()
    db_url = "{}+{}://{}:{}@{}:{}/{}?charset={}".format(db_args.get('type'),
                                                        db_args.get('connect_type'), db_args.get('username'), db_args.get('password'), db_args.get('host'),
                                                        db_args.get('port'), db_args.get('db_name'), db_args.get('charset'))
    print(db_url)
    return create_engine(db_url)


engine = get_engine()
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base()
metadata = MetaData(get_engine())

__all__ = ['Base', 'metadata', 'engine', 'db_session']