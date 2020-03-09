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