while True:
    try:
        n = int(input())
        for i in range(n):
            t = int(input())
            a = []
            for j in range(2*t):
                a.append(list(map(int, input().split(' '))))
                print(a)
    except:
        break