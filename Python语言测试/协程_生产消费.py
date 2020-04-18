import time

def producer(c):
    c.__next__()
    for i in range(10):
        c.send(i)
        time.sleep(1)


def consumer():
    while 1:
        a = yield
        print("消费了："+str(a))


a = consumer()
producer(a)