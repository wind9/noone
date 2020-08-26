import logging
from logging.handlers import RotatingFileHandler
import os


log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'snw.log')
log = logging.getLogger("snw")
log.setLevel(logging.INFO)
file_handler = RotatingFileHandler(filename=log_file_path, encoding='utf-8')
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
log.addHandler(file_handler)
log.addHandler(console_handler)

