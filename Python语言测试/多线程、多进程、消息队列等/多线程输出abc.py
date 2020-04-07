import threading

a_lock = threading.Lock()
b_lock = threading.Lock()
c_lock = threading.Lock()

def print_a():
    while 1:
        c_lock.acquire()
        print('a',end='')
        a_lock.release()

def print_b():
    while 1:
        a_lock.acquire()
        print('b',end='')
        b_lock.release()

def print_c():
    while 1:
        b_lock.acquire()
        print('c')
        c_lock.release()


a = threading.Thread(target=print_a)
b = threading.Thread(target=print_b)
c = threading.Thread(target=print_c)

a_lock.acquire()
b_lock.acquire()
a.start()
b.start()
c.start()

