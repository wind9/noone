from local_test.task1 import do_test
import random
from workers import app


for i in range(1, 1000):

    x = random.randint(0, 100)
    y = random.randint(0, 100)
    # do_test.delay()
    app.send_task('local_test.task1.do_test', queue='task1_queue', routing_key='task1_routing', args=())

