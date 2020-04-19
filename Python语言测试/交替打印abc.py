from threading import Thread, Lock


def printA(lockC,lockA):
    for i in range(10):
        lockC.acquire()
        print("A")
        lockA.release()

def printB(lockA,lockB):
    for i in range(10):
        lockA.acquire()
        print('B')
        lockB.release()

def printC(lockB,lockC):
    for i in range(10):
        lockB.acquire()
        print('C')
        lockC.release()

lock_a = Lock()
lock_b = Lock()
lock_c = Lock()

a = Thread(target=printA,args=(lock_c,lock_a))
b = Thread(target=printB,args=(lock_a,lock_b))
c = Thread(target=printC,args=(lock_b,lock_c))

lock_a.acquire()
lock_b.acquire()
a.start()
b.start()
c.start()
