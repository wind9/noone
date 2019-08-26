from tasks.workers import app
from db.dao import LoginInfoOper
from db.cookies_db import Cookies
from logger import weibo
from login import get_session
import time


def login_task(name,password):
    get_session(name,password)


@app.task(ignore_result=True)
def execute_login_task():
    login_infos = LoginInfoOper.get_login_info()
    Cookies.check_login_task()
    weibo.info("The login task is starting...")
    for login_info in login_infos:
        app.send_task('tasks.login.login_task', args=(login_info.name,login_info.password), queue='login_queue',
                      routing_key='for_login')
        time.sleep(10)

