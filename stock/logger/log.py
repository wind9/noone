import logging
from logging import config as log_conf
import os

log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_path = os.path.join(log_dir, 'stock.log')

log_config = {
    "version": 1.0,
    "formatters": {
        "sample": {
            'format': '%(asctime)s|%(name)s|%(levelname)s|%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        "detail": {
            'format': '%(asctime)s|%(name)s|%(levelname)s|%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detail'
        },
        "file": {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detail',
            'filename': log_path,
            'encoding': 'utf-8',
            'maxBytes': 1024*1024*5,
            'backupCount': 10,
        }
    },
    "loggers": {
        'storage': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
        'common': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
    },
}

log_conf.dictConfig(log_config)

storage = logging.getLogger('storage')