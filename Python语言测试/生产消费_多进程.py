from multiprocessing import Process, Queue
import time, random

def producer(queue):
    for i in range(10000):
        tem = random.randint(1,1000)
        queue.put(tem)
        print("生产了："+str(tem))
        # time.sleep(1)


def consumer(queue):
    while True:
        time.sleep(5)
        tem = queue.get()
        if not tem:
            print("队列为空")
        else:
            print("消费了："+str(tem))

if __name__ == "__main__":
    q = Queue(100)
    p = Process(target=producer,args=(q,))
    c = Process(target=consumer,args=(q,))
    p.start()
    c.start()