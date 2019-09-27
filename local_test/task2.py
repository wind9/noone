from .workers import app


@app.task
def do_test():
    print("正在测试task2")
