m, k = list(map(int,input().split()))
data = input().split()
dataInt = list(map(int,data))
if m == k:
    print(' / '.join(data))
else:
    sumData = sum(dataInt)/k
    res = []
    s = 0
    for i in range(m):
        s = s + dataInt[i]
        if s > sumData and k>1:
            k -= 1
            res.append('/')
            res.append(data[i])
            s = dataInt[i]
        else:
            res.append(data[i])
    print(' '.join(res))