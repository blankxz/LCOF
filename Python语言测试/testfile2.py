m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(*m)
print(m)
print(list(zip(*m)))
print(list(zip(*m))[::-1])

print(*(1,2))

res = []
res.append(i for i in [1,2,3,4,5])
print(res)

print(5//2)

students = [('john', 'A', 9), ('jane', 'B', 12), ('dave', 'B', 10)]
aa = sorted(students, key=lambda s:s[2])
print(aa)