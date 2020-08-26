from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_mysql_args, get_redis_args
from redis import StrictRedis, ConnectionPool


def get_database_uri():
    mysql_args = get_mysql_args()
    uri = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(mysql_args.get('user'),
                                                                mysql_args.get('password'), mysql_args.get('host'), mysql_args.get('port'), mysql_args.get('db'))
    return uri


def get_engine():
    database_uri = get_database_uri()
    engine = create_engine(database_uri)
    return engine


def get_filter_redis():
    redis_args = get_redis_args()
    redis_uri = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('filter_db'))
    pool = ConnectionPool.from_url(redis_uri)
    filter_redis = StrictRedis(connection_pool=pool)
    return filter_redis


engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
metadata = MetaData(get_engine())
db_session = Session()
filter_redis = get_filter_redis()
