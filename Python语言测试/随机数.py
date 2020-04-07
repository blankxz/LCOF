import random


a = list(range(1,101))
for i in range(5):
    b = random.choice(a)
    a.remove(b)
    print(b)
