from celery import Celery
from kombu import Exchange, Queue
from config import get_redis_args
import os

redis_args = get_redis_args()
redis_password = redis_args.get('password')
redis_host = redis_args.get('host')
redis_port = redis_args.get('port')
broker_db = redis_args.get('broker_db')
backend_db = redis_args.get('backend_db')
broker_uri = "redis://:{}@{}:{}/{}".format(redis_password, redis_host, redis_port, broker_db)
backend_uri = "redis://:{}@{}:{}/{}".format(redis_password, redis_host, redis_port, backend_db)
worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'worker.log')
#beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'worker.log')

tasks = ['tasks.do_article', 'tasks.do_user', 'tasks.do_comment']

app = Celery("jsl_task", broker=broker_uri, backend=backend_uri, include=tasks)
app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_LOG_FILE=worker_log_path,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',
    CELERY_QUEUES=(
        Queue('article_queue', exchange=Exchange('article_exchange', type='direct'), routing_key='article'),
        Queue('comment_queue', exchange=Exchange('comment_exchange', type='direct'), routing_key='comment'),
        Queue('article_queue', exchange=Exchange('article_exchange', type='direct'), routing_key='user'),
    )
)