import logging
from logging.handlers import RotatingFileHandler
import os

log_dir_path = os.path.dirname(os.path.dirname(__file__))+'/logs'
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path)
log_file_path = os.path.join(log_dir_path, 'snw.log')
log = logging.getLogger("snw")
log.setLevel(logging.INFO)
file_handler = RotatingFileHandler(filename=log_file_path, encoding='utf-8')
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
log.addHandler(file_handler)
log.addHandler(console_handler)

