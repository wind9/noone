from celery import Celery
import time
from kombu import Queue, Exchange
from datetime import timedelta

redis_host = '121.15.10.34'
redis_port = 8912
redis_pass = 'rt0755'
broker_db = 3
backend_db = 4
broker_url = "redis://:{}@{}:{}/{}".format(redis_pass, redis_host, redis_port, broker_db)
backend_url = "redis://:{}@{}:{}/{}".format(redis_pass, redis_host, redis_port, backend_db)
tasks = ['local_test.task1', 'local_test.task2', 'local_test.task3']
app = Celery("ceshi_tasks", include=tasks, broker=broker_url, backend=backend_url)


app.conf.update(
    CELERY_QUEUES=(
        Queue('task1_queue', exchange=Exchange('task1_ex', type='direct'), routing_key='task1_routing'),
        Queue('task2_queue', exchange=Exchange('task2_ex', type='direct'), routing_key='task2_routing'),
        Queue('task3_queue', exchange=Exchange('task3_ex', type='direct'), routing_key='task3_routing'),
    )
)

