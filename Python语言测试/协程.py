import time

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         time.sleep(1)
#         r = '200 OK'

# def produce(c):
#     print(next(c)+"----")
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()

# if __name__=='__main__':
#     c = consumer()
#     produce(c)
    
    
# def a():
#     print('aaa')
#     p1 = yield '123'
#     print('bbb')
#     if (p1 == 'hello'):
#         print('p1是send传过来的')
#     p2= yield '234'
#     print(p2)

# r = a()
# print(next(r))
# print('==========')
# r.send('hello')
# print(r.send('你好'))

# #结果为
# aaa
# bbb
# p1是send传过来的


def con():
    res = ''
    while True:
        n = yield res
        if not n:
            return
        print("consume ing")
        print(n)
        time.sleep(1)
        res = 'oK'


def pro(c):
    next(c)
    print('start')
    for i in range(1,5):
        print('product ing')
        r = c.send(i)
        print(r)
    c.close()
c = con()
pro(c)

