from threading import Thread

num = []


def add_num():
    global num
    for i in range(100000):
        num += [1]


if __name__ == '__main__':
    t1 = Thread(target=add_num)
    t2 = Thread(target=add_num)
    t3 = Thread(target=add_num)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(len(num))