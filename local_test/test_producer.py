from local_test.task1 import do_test
import random


for i in range(1, 1000):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    do_test.delay()

