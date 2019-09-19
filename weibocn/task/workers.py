from celery import Celery
from config import get_redis_args
from kombu import Queue, Exchange
from logger import weibo
import os

worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/logs', 'worker.log' )
beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/logs', 'beat.log' )
redis_args = get_redis_args()
broker_url = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('broker_db'))
tasks = ["task.cookies"]

app = Celery("workers", include=tasks, broker=broker_url)
app.conf.update(
    CELERY_ENABLE_UTC = True,
    CELERY_TIMEZONE = "Asia/Shanghai",
    CELERY_RESULT_SERIALIZER = 'json',
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_LOG_FILE = worker_log_path,
    CELERYBEAT_LOG_FILE = beat_log_path,
    CELERY_QUEUES = (
        Queue('cookies_queue', exchange=Exchange('cookies_queue', type='direct'), routing_key='for_cookies'),
    )
 )



