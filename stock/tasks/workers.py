from celery import Celery
from config import get_celery_args


celery_args = get_celery_args()
broker_url = celery_args.get('broker')
backend_url = celery_args.get('backend')

#tasks = ['tasks.stock']

app = Celery('stock', broker=broker_url, backend=backend_url)

