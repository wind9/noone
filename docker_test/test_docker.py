import random

for i in range(100):
    print("get random number: %s" % random.randint(0, 100))

with open("ok.txt", "w") as f:
    print("test docker success")
    print("test docker ignore")

