from threading import Thread,Semaphore
import threading
import time


def task():
    sm.acquire()
    print(f"{threading.current_thread().name} get sm")
    time.sleep(3)
    sm.release()

if __name__ == '__main__':
    sm = Semaphore(5) # 同一时间只有5个进程可以执行。
    for i in range(20):
        t = Thread(target=task)
        t.start()