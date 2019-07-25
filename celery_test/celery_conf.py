BROKER_URL = 'redis://192.168.88.200:6379/0'
CELERY_RESULT_BACKEND = 'redis://192.168.88.200:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = {
    'celery_test.task1',
    'celery_test.task2'
}


CELERY_SCHEDULE = {
    'dingshirenwu1':{
        'task': 'celery_test.task1',
        'schedule': timedeta(seconds=30),
        'args': (5, 8)
    }
}