from celery import Celery
from kombu import Queue, Exchange
from config import get_redis_args
import os

redis_args = get_redis_args()
broker_uri = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('broker_db'))
backend_uri = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('backend_db'))
tasks = ["tasks.brand", "tasks.area"]
app = Celery("test_celery", backend=backend_uri, broker=broker_uri, include=tasks)
worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'worker.log')

app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_LOG_FILE=worker_log_path,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',
    CELERY_QUEUE=(
        Queue("area", exchange=Exchange("exchange1", type="direct"), routing_key="route1"),
        Queue("queue2", exchange=Exchange("exchange2", type="direct"), routing_key="route2"),
    )
)