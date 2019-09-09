import random
from .workers import import appdirs


task_num = 10
for i in range(task_num):
    x = random.randint(0,100)
    y = random.randint(0,100)
    app.send_tasks()