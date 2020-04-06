from threading import Thread, Lock
import os, time


def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n)  # 结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全