from celery import Celery
from kombu import Queue, Exchange
from config import get_redis_args
import os

redis_args = get_redis_args()
broker_uri = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('broker_db'))
backend_uri = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('backend_db'))
app = Celery("test_celery", backend=backend_uri, broker=broker_uri, include=["tasks.task1", "tasks.task2"])
worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'worker.log')

app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_LOG_FILE=worker_log_path,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',
    CELERY_QUEUE=(
        Queue("task1_queue", exchange=Exchange("exchange1", type="direct"), routing_key="route1"),
        Queue("task2_queue", exchange=Exchange("exchange2", type="direct"), routing_key="route2"),
    )
)