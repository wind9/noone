from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_mysql_args, get_redis_args


def get_engine():
    mysql_args = get_mysql_args()
    uri = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(
        mysql_args.get('user'), mysql_args.get('password'), mysql_args.get('host'), mysql_args.get('port'),
        mysql_args.get('db')
    )
    #print(uri)
    return create_engine(uri)


engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()
metadata = MetaData(get_engine())


