t = int(input())
for i in range(t):
    q = int(input())
    a = []
    for j in range(q):
        operation = input()
        if operation == 'TOP':
            if not a:
                print(-1)
            else:
                print(a[0])
            continue
        if operation == 'POP':
            if not a:
                print(-1)
            else:
                a.pop(0)
            continue
        if operation == 'SIZE':
            print(len(a))
            continue
        if operation == 'CLEAR':
            a = []
            continue
        b = int(operation.split()[1])
        a.append(b)