from functools import reduce

print(list(filter(lambda x:x>2,[i for i in range(10)])))

print(list(map(lambda x:x*x,[i for i in range(5)])))

print(reduce(lambda x,y:x*y,[i for i in range(5)]))