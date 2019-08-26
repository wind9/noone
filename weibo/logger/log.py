import logging
from logging import config as log_conf
import os


log_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)) + '/logs')

if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_path = os.path.join(log_dir, 'weibo.log')

log_config_dict = {
    'version': 1.0,
    'formatters': {
        'simple': {
            'formatter': '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'details': {
            'formatter': '%(asctime)s-%(levelname)s-%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 5,
            'maxBytes': 1024*1024,
            'filename': log_path,
            'level': 'INFO',
            'encoding': 'utf8',
            'formatter': 'detail'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'detail'
        }
    },
    'loggers': {
        'store': {
            'handlers': ['file', 'console'],
            'level': 'INFO'
        }
    }
}

log_conf.dictConfig(log_config_dict)

weibo = logging.getLogger('weibo')
