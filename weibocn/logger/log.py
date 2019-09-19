import logging
from logging import config
import os


log_dir_path = os.path.dirname(os.path.dirname(__file__)) + '/logs'
if not os.path.exists(log_dir_path):
    os.mkdir(log_dir_path)
log_file_path = os.path.join(log_dir_path, 'weibo.log')


log_con_dict = {
    "version": 1.0,
    "formatters": {
        "detail": {
            "format": "%(asctime)s-%(levelname)s-%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "sample": {
            "format": "%(asctime)s-%(levelname)s-%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": log_file_path,
            "backupCount": 5,
            "maxBytes": 1024*1024*5,
            "encoding": "utf-8",
            "level": "INFO"
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO"
        }
    },
    "loggers": {
        "weibo": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "formatter": "detail",
        }
    }
}

config.dictConfig(log_con_dict)
weibo = logging.getLogger("weibo")