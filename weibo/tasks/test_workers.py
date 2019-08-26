from kombu import Exchange, Queue
from celery import Celery
from config import get_broker_and_backend, get_redis_master
import os
from datetime import timedelta


worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/logs', 'worker.log')
beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/logs', 'beat.log')

tasks = ['tasks.login.execute_login']
broker_and_backend = get_broker_and_backend()
if isinstance(broker_and_backend, tuple):
    broker_url, backend_url = broker_and_backend
    app = Celery('workers', include=tasks, broker=broker_url, backend=backend_url)
else:
    app = Celery('workers', include=tasks, broker=broker_and_backend)
    master = get_redis_master()
    app.conf.update(
        BROKER_TRANSPORT_OPTIONS={'master_name':master}
    )

app.conf.update(
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_LOG_FILE=worker_log_path,
    CELERYBEAT_LOG_FILE=beat_log_path,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',
    CELERY_SCHUDULER={
        'login_task': {
            'task': 'tasks.login.execute_login_task',
            'schedule': timedelta(hours=2),
            'options': {'queue': 'login_queue','routing_key': 'for_login'}
        },
        'user_task': {
            'task': '',
            'schedule': timedelta(minutes=2),
            'options': {'queue': 'user_queue','routing_key': 'for_user'}
        },
    },
    CELERY_QUEUES={
        Queue('login_queue', Exchange('for_login', type='direct'), routing_key='for_login')
    }

)
