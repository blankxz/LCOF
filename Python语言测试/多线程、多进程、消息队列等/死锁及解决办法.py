from threading import Thread, Lock
import time

mutex_x = Lock()
mutex_y = Lock()


def x_func():
    print('X...')
    mutex_x.acquire()
    print('Lock x something')
    time.sleep(1)

    result = mutex_y.acquire(timeout=10)
    print(result)
    print('Use y something')
    time.sleep(1)
    if result:
        mutex_y.release()

    print('x...')
    mutex_x.release()


def y_func():
    print('Y...')
    mutex_y.acquire()
    print('Lock y something')
    time.sleep(1)
    mutex_x.acquire()
    print('Use x something')
    time.sleep(1)
    mutex_x.release()
    print('y...')
    mutex_y.release()


if __name__ == '__main__':
    t1 = Thread(target=x_func)
    t2 = Thread(target=y_func)

    t1.start()
    t2.start()