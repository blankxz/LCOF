a = int(input())
for i in range(a):
    b = int(input())
    dataA = []
    for j in range(b):
        dataA.append(list(map(int,input().split())))
    dataB = []
    for j in range(b):
        dataB.append(list(map(int, input().split())))
    dataA.sort(key=lambda j: j[1])
    dataB.sort(key=lambda j: j[1])
    res = -1
    for x in dataA:
        flag = 0
        for y in dataB:
            r = (x[0]-y[0])**2+(x[1]-y[1])**2
            if res == -1:
                res = r
            if r <= res:
                res = r
            else:
                flag += 1
                if flag >100:
                    break
    print("%.3f"%res**0.5)

