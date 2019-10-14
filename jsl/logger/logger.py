import logging
from logging import config as log_config
import os

log_dir = os.path.dirname(os.path.dirname(__file__)) + '/logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_file_path = os.path.join(log_dir, 'jsl.log')

log_conf_dict = {
    'version': 1.0,
    "formatters": {
        "detail": {
            "format": "%(asctime)s|%(name)s|%(levelname)s|[%(message)s]",
            "datefmt": "%Y-%m-%d %H:%M:%S.%f"
        },
        "sample": {
            "format": "%(asctime)s|[%(message)s]",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "sample",
            "level": "INFO"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detail",
            "level": "INFO",
            "filename": log_file_path,
            "encoding": "utf-8",
            "maxBytes": 1024*1024*1024,
            "backupCount": 5,
        }
    },
    "loggers": {
        "common": {
            "handlers": ["file", "console"],
            "level": "INFO"
        },
        "jsl": {
            "handlers": ["file"],
            "level": "INFO"
        }
    }
}

log_config.dictConfig(log_conf_dict)
jsl_log = logging.getLogger("jsl")
