n = int(input())
a = list(map(float,input().split( )))
b = list(map(float,input().split( )))
sum = 0
for i in range(n):
    sum += a[0]**(i+1)*b[0]

sum2 = 0
nn = int(n//b[1])
for i in range(nn):
    sum2 += a[1] ** (i + 1) * b[1]
if nn*b[1] < n:
    for i in range(n-nn*b[1]):
        sum2 += a[0] ** (i + 1) * b[0]
if sum2>sum:
    print('%.2f'%sum2)
else:
    print('%.2f' % sum)