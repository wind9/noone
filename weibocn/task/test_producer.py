import random
#from task.login import execute_gen_cookies
from task.workers import app
import time


if __name__ == '__main__':
    task_num = 10
    app.send_task("task.cookies.execute_gen_cookies", args=(), queue="cookies_queue", routing_key="for_cookies")
    time.sleep(3)
        #execute_gen_cookies.apply_async((x, y))
