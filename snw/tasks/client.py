from tasks import app

if __name__ == '__main__':
    app.send_task("tasks.task1.do_task1", args=(3,4,), queue='task1_queue', routing_key='route1')
    print("send done")
