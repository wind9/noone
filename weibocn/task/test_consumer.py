from .workers import app


@app.task
def test(x, y):
    print("收到参数x：%s,y:%s" % (x,y))
    return x + y
