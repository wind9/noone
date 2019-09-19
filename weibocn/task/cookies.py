from login import get_cookies
from task.workers import app
from db.redis_db import Cookies
import json
import time


@app.task(ignore_result=True)
def execute_gen_cookies():
    cookies_dict = get_cookies()
    gen_time = time.time()
    json_str = json.dumps({"gen_time": gen_time, "login": cookies_dict})
    Cookies.store_cookies(json_str)




