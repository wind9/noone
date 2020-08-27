from tasks import app
from db import CommonOper
from logger import log
import json


@app.task()
def save_data(title, datas):
    log.info("{},数据正在存储".format(title))
    CommonOper.add_all(json.loads(datas))
