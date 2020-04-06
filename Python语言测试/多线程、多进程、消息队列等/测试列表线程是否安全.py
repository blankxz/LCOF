from threading import Thread

num = []


def add_num():
    # global num
    for i in range(100000):
        num.append(1)
    print('stop')


if __name__ == '__main__':
    print('main_start')
    t1 = Thread(target=add_num)
    t2 = Thread(target=add_num)
    t3 = Thread(target=add_num)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()

    print('main_stop')
    print(len(num))