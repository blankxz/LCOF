import random
import multiprocessing


def producer(queue):  # 生产者生产数据
    for __ in range(10):
        queue.put(random.randrange(100))


def consumer(queue):  # 消费者处理数据
    while True:
        if not queue.empty():
            item = queue.get()  # 模拟消费者的处理过程
            print("处理一个元素：{}".format(item))


if __name__ == "__main__":
    queue = multiprocessing.Queue()

    proProcess = multiprocessing.Process(target=producer, args=(queue,))
    conProcess = multiprocessing.Process(target=consumer, args=(queue,))
    proProcess.start()
    conProcess.start()

    proProcess.join()
    while not queue.empty():  # 当队列不为空时，继续等待消费者处理
        pass
    conProcess.terminate()  # 终止消费者进程
    print("处理结束")

