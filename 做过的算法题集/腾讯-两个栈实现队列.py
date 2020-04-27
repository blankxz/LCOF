t = int(input())
a = []
for i in range(t):
    operation = input()
    if operation == 'peek':
        print(a[0])
        continue
    if operation == 'poll':
        a.pop(0)
        continue
    b = int(operation.split()[1])
    a.append(b)