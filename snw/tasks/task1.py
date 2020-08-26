from tasks import app


@app.task()
def do_task1(x, y):
    print("收到任务{}+{}".format(x, y))
    return x + y
