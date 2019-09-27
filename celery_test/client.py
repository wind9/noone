from celery_test import task1
from celery_test import task2

username = 'test_user'
password = 'test_password'
task1.send_mail.apply_asyn(args=(username, password),countdown = 5)
task2.send_notice.apply_asyn(args=(username, password))
print('任务已发送')


