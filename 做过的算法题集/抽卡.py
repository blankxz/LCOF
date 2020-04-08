n = int(input())
data = []
while n:
    n-=1
    data.append(list(map(int,input().split())))
data.sort(key=lambda i:i[1],reverse=True)
data1 = []
data2 = []
for i in range(len(data)):
    if data[i][1]==0:
        data1 = data[:i]
        data2 = data[i:]
        break
if data2 and data1:
    data2.sort(key=lambda j:j[0],reverse=True)
    data = data1+data2
if not data2 and data1:
    data = data1
if data2 and not data1:
    data2.sort(key=lambda j: j[0], reverse=True)
    data = data2

temp = data[0][1]
money = data[0][0]
if len(data) == 1:
    print(money)
else:
    for i in range(1,len(data)):
        if temp == 0:
            break
        else:
            temp = temp -1 + data[i][1]
            money += data[i][0]
    print(money)
