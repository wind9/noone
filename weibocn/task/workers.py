from celery import Celery
from config import get_redis_args


redis_args = get_redis_args()
broker_url = "redis://:{}@{}:{}/{}".format(redis_args.get('password'), redis_args.get('host'), redis_args.get('port'), redis_args.get('broker_db'))

app = Celery("workers", broker=broker_url)
# app.conf.update(
#     CELERY_ENABLED = True,
#     CELERY_TIMEZONE = "Asia/Shanghai",
#     CELERY_BACKEND_SERIAZIED = 'json'
# )


