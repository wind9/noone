from celery_test import app


@app.task
def send_notice(username, password):
    return '通知已发送，用户名%s,密码:%s'%(username, password)
