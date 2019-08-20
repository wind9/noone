from .workers import app
from db.dao import LoginInfoOper

@app.task(ignore_result=True)
def execute_login_task():
    infos = LoginInfoOper.get_login_info()
