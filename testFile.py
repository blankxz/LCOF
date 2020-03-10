print([i **2 for i in [1,2,3,4,5,6,7,8,9][-2::-2]])


a = [1,2,5,4,8,6,5]

a.sort()
print(a)
a = [1,2,5,4,8,6,5]
a = sorted(a)
print(a)


a = 1
print(id(a))
def fun(a):
    print(id(a))
    a = 2
    
fun(a)
print(a)

a = []
print(id(a))
def fun(a):
    print(id(a))
    a.append(1)
fun(a)
print(a)

# Python的变量就是在特定的时间引用了一个特定的对象。

def print_1():
    a = '11223'
    def print_2():
        print(a)
    return print_2
print_1()()

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper

# @log
def test(p):
    print(test.__name__ + " param: " + p)
    
# test("I'm a param")

w = log(test)
w('111')


def log(level):
    def info(func):
        
        def say(*args, **kwargs):
            print("[DEBUG]: enter {}()".format(func.__name__))
            print(level)
            return func(*args, **kwargs)
        return say
    return info


@log('1')
def hello(a):
    print(a)
    
@log('2')
def by():
    print('by')
    
hello('aaa')
by()


def dict(**kwargs):
    print(kwargs)
    return kwargs
 
mydict = dict(system="系统", China="中国", link="联接")
x = 'system'
if x in mydict:
    print(x)
    print("中文意思：", mydict[x])
else:
    print("抱歉，没找到。")