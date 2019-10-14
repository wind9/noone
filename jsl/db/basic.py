from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import get_mysql_args, get_redis_args
from redis import StrictRedis, ConnectionPool


def get_engine():
    mysql_args = get_mysql_args()
    uri = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(
        mysql_args.get('user'), mysql_args.get('password'), mysql_args.get('host'), mysql_args.get('port'),
        mysql_args.get('db')
    )
    #print(uri)
    return create_engine(uri)


def get_filter_redis():
    redis_args = get_redis_args()
    filter_redis_uri = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'),
                                              redis_args.get('port'), redis_args.get('filter_db'))
    pool = ConnectionPool.from_url(filter_redis_uri)
    filter_redis = StrictRedis(connection_pool=pool)
    return filter_redis


filter_redis = get_filter_redis()
engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()
metadata = MetaData(get_engine())


