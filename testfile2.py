m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(*m)
print(m)
print(list(zip(*m)))
print(list(zip(*m))[::-1])

print(*(1,2))

res = []
res.append(i for i in [1,2,3,4,5])
print(res)