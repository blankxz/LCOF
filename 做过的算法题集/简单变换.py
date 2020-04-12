t = int(input())
for m in range(t):
    # 读取每一行
    n = int(input())
    a = list(map(int,input().split(' ')))
    b = list(map(int,input().split(' ')))
    if a == b:
        print('YES')
        continue
    l = 0
    r = n - 1
    flag = 0
    for i in range(n):
        if a[i] != b[i] and flag == 0:
            l = i
            flag = 1
            continue
        if a[i] == b[i] and flag == 1:
            r = i
            break
    temp = b[l]-a[l]
    for i in range(l,r):
        a[i] += temp
    if a == b:
        print('YES')
    else:
        print('NO')


while b:
    if cur < l:
        t  = list(filter(lambda x : x < a[cur] , b))
        ll = len(t)
        dic[a[cur-1]] = t
        cur += 1
        b = b[ll:]
    else:
        dic[a[cur-1]] = b
        b = []
money = 0
# print(dic)
for i in dic:
    money += (sum(dic[i])-len(dic[i])*i)
print(money)