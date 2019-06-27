from celery import Celery

app = Celery('tasks', broker='redis://192.168.88.200:6379/0')


@app.task
def send_mail(email):
    print("send mail to ", email)
    import time
    time.sleep(4)
    return "success"
