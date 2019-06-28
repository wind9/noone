from celery_test import app


@app.task
def send_mail(username, password):
    return '邮件已发送，用户名%s,密码:%s'%(username, password)
