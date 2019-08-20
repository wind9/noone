from celery import Celery
from kombu import Exchange, Queue
from datetime import timedelta
import os
from config import get_broker_and_backend, get_redis_master

beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/logs', 'beat.log')
worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/logs', 'worker.log')
broker_and_backend = get_broker_and_backend()

tasks = ['tasks.login', 'tasks.user']

if isinstance(broker_and_backend, tuple):
    broker, backend = broker_and_backend
    app = Celery('weibo_task', include=tasks, broker=broker, backend=backend)
else:
    master = get_redis_master()
    app = Celery('weibo_task', include=tasks, broker=broker_and_backend)
    app.conf.update(
        BROKER_TRANSPORT_OPTIONS={'master_name': master},
    )

app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_LOG_FILE=worker_log_path,
    CELERYBEAT_LOG_FILE=beat_log_path,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',
    CELERY_SCHEDULER={
        'login_task': {
            'task': 'tasks.login.execute_login_task',
            'schedule': timedelta(hours=20),
            'options': {'queue': 'login_queue', 'routing_key': 'for_login'}
        },
        'user_task': {
            'task': 'tasks.user.execute_user_task',
            'schedule': timedelta(minutes=10),
            'options': {'queue':'user_queue', 'routing_key': 'for_user'}
        }
    },
    CELERY_QUEUES=(
        Queue('login_queue', exchange=Exchange('login_queue',type='direct'),routing_key='for_login'),
        Queue('user_queue', exchange=Exchange('user_queue',type='direct'),routing_key='for_user'),
    )
)
