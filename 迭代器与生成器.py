a = [i for i in range(10)]
print(a)

a = (i for i in range(10))
print(a)
print(next(a))

def gen():
    for i in range(10):
        yield i
        
a = gen()
print(a)