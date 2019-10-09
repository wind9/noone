from celery import Celery
import time
from kombu import Queue, Exchange
from datetime import timedelta

redis_host = '121.15.10.34'
redis_port = 8912
redis_pass = 'rt0755'
broker_db = 0
backend_db = 1
broker_url = "redis://:{}@{}:{}/{}".format(redis_pass, redis_host, redis_port, broker_db)
backend_url = "redis://:{}@{}:{}/{}".format(redis_pass, redis_host, redis_port, backend_db)
tasks = ['local_test.task1', 'local_test.task2', 'local_test.task3']
app = Celery("ceshi_tasks", include=tasks, broker=broker_url, backend=backend_url)


app.conf.update(
    CELERY_QUEUES=(
        Queue('task1_queue', exchange=Exchange('task1_ex', type='direct'), routing_key='task1_routing'),
        Queue('task2_queue', exchange=Exchange('task2_ex', type='direct'), routing_key='task2_routing'),
        Queue('task3_queue', exchange=Exchange('task3_ex', type='direct'), routing_key='task3_routing'),
    ),
    CELERYBEAT_SCHEDULE={
        'test1_task': {
            'task': 'local_test.task1.do_test',
            'schedule': timedelta(seconds=1),
            'options': {'queue': 'task1_queue', 'routing_key': 'task1_routing'}
        },
        'test2_task': {
            'task': 'local_test.task2.do_test',
            'schedule': timedelta(seconds=2),
            'options': {'queue': 'task2_queue', 'routing_key': 'task2_routing'}
        },
        'test3_task': {
            'task': 'local_test.task3.do_test',
            'schedule': timedelta(seconds=3),
            'options': {'queue': 'task3_queue', 'routing_key': 'test3_key'}
        },
    }
)

