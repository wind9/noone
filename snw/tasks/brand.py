from tasks import app


@app.task()
def do_task2(x, y):
    return x*y
