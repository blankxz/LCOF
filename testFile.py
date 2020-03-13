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
    
    
    

def quick(arr,left,right):
    if arr == []:
        return
    if left > right:
        return 
    key = arr[left]
    l = left
    r = right
    while l!=r:
        
        while arr[r]>=key and l<r:
            r -= 1
        while arr[l]<=key and l<r:
            l += 1
        if l<r:
            arr[l],arr[r] = arr[r],arr[l]
    arr[left], arr[l] = arr[l], arr[left]
    quick(arr,left,l-1)
    quick(arr,l+1,right)
    
a = [1,5,7,8,3]
quick(a,0,4)
print(a)

a = [1,5,7,8,3]
def quick2(a):
    if len(a)<2: return a
    key = a[len(a)//2]
    l = []
    r = []
    a.remove(key)
    for i in a:
        if i<key:
            l.append(i)
        else:
            r.append(i)
    return quick2(l)+[key]+quick2(r)

print(quick2([1,5,7,8,3]))


m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(*m)
print(m)