while 1:
    a = input().split()
    n = int(a[0])
    m = int(a[1])
    nn = input().split()
    nn = [int(i) for i in nn]
    for i in range(m):
        t = int(input())
        while 1:
            if t in nn:
                t+=1
            else:
                print(t)
                break

