import sys

name = ["alpha", "beta", "gamma"]
age = [10, 20, 30]

size1 = sys.getsizeof(name) + sys.getsizeof(name)

print(size1)

stu = {"alpha": 10, "beta": 20, "gamma": 30}
size2 = sys.getsizeof(stu)
print(size2)