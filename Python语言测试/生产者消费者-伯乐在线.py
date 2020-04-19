from threading import Thread,Lock
from queue import Queue
from random import randint
import time

class Producer(Thread):
    def __init__(self,queue,maxSize,lockB,lockC):
        super().__init__()
        self.queue = queue
        self.maxSize = maxSize
        self.lockB = lockB
        self.lockB.acquire()
        self.lockC = lockC
        self.lockC.acquire()

    def run(self):
        while 1:
            data = randint(1,100)
            print("生产了：" + str(data))
            self.queue.put(data, block=True)
            if data % 3 == 0:
                self.lockB.release()
            else:
                self.lockC.release()
            time.sleep(1)

class ConsumerB(Thread):
    def __init__(self, queue,lock):
        super().__init__()
        self.lock = lock
        self.queue = queue

    def run(self):
        while 1:
            self.lock.acquire()
            data = self.queue.get()
            print("B 消费了：" + str(data))
            self.lock.release()
            self.lock.acquire()

class ConsumerC(Thread):
    def __init__(self, queue, lock):
        super().__init__()
        self.lock = lock
        self.queue = queue

    def run(self):
        while 1:
            self.lock.acquire()
            data = self.queue.get()
            print("C 消费了：" + str(data))
            self.lock.release()
            self.lock.acquire()

if __name__ == "__main__":
    queue = Queue(100)
    lockB = Lock()
    lockC = Lock()
    producer = Producer(queue,10,lockB,lockC)
    producer.start()
    consumerB = ConsumerB(queue,lockB)
    consumerB.start()
    consumerC = ConsumerC(queue, lockC)
    consumerC.start()