
try:
    while True:
        n = int(input())
        data = []
        for i in range(n):
            a = int(input())
            data.append(a)
        data = list(set(data))
        data.sort()
        for i in data:
            print(i)

except:
    pass