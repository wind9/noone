BROKER_URL = 'redis://192.168.88.200:6379/0'
CELERY_RESULT_BACKEND = 'redis://192.168.88.200:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = {
    'celery_test.task1',
    'celery_test.task2'
}