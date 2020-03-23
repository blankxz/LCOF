data = []
while 1:
    a = input()
    data.append(list(a))
    if len(data) == 3:
        temp = data.copy()
        for i in range(3):
            data[i] = data[2-i][::-1]
        if temp == data:
            print('YES')
        else:
            print('NO')
        data = []