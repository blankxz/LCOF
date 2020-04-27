n = int(input())
data = []
for i in range(n):
    x, k = list(map(int,input().split()))
    n = 0
    while 1:
        if x<2**n:
            break
        else:
            n +=1
    if k>=n:
        print(-1)
        continue
    else:
        while k!=n:
            n -= 1
            x //= 2
        print(x)