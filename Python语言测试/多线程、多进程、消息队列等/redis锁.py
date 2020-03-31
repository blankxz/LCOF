from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='12345')
redis.delete('p_t_l')

# redis.set('name', 'Bob')
# print(redis.get('name'))

import threading

money = 0
def Order(n):
    global money
    money = money + n
    money = money - n

class thread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='线程' + threadname)
        self.threadname = int(threadname)

    def run(self):
        for i in range(10000):
            print(i)
            while 1:
                if redis.setnx('p_t_l',1):
                    break
                else:
                    continue
            Order(self.threadname)
            redis.delete('p_t_l')
#        print('%s:Now timestamp is %s'%(self.name,time.time()))

lock = threading.Lock()
t1 = thread('1')
t2 = thread('5')
t1.start()
t2.start()

print(money)