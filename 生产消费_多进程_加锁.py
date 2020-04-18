from multiprocessing import Lock,Process,Queue,Condition
import time

class Producer(Process):
    def __init__(self, maxSize, q, lock,con):
        super().__init__()
        self.q = q
        self.maxSize = maxSize
        self.lock = lock
        self.con = con

    def run(self):
        time.sleep(2)
        for i in range(1000):
            self.lock.acquire()
            self.q.put(i)
            print("生产了："+str(i))
            self.con.notify()
            self.lock.release()

class Consumer(Process):
    def __init__(self, queue, lock,con):
        super().__init__()
        self.queue = queue
        self.lock = lock
        self.con = con

    def run(self):
        for i in range(1000):
            self.lock.acquire()
            if self.queue.qsize() == 0:
                print("队列为空")
                self.con.wait()
            else:
                print("消费了："+ str(self.queue.get()))
            self.lock.release()

if __name__ == "__main__":
    q = Queue()
    l = Lock()
    con = Condition(l)
    p = Producer(1000,q,l,con)
    c = Consumer(q,l,con)
    p.start()
    c.start()

