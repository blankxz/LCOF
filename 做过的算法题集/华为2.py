data = input().split()
ind_5a = []
for i in range(len(data)):
    if data[i] == '5a':
        ind_5a.append(i)
if not ind_5a or len(ind_5a)==1:
    print('')
else:
    dataList = []
    for i in range(len(ind_5a)-1):
        dataList.append(data[ind_5a[i]:ind_5a[i+1]])
    dataL2 = []
    for i in dataList:
        if i:
            i.pop(0)
            dataL2.append(i)
    dataList = dataL2
    res = []
    for i in dataList:
        num = 0
        for j in range(len(i)-1):
            if i[j] == '5b':
                continue
            else:
                num += 1
        try:
            if num == int(i[-1]):
                res.append(i)
        except:
            pass
    r = '5a '
    for i in res:
        r += ' '.join(i)
        r += ' 5a '
    print(r[:-1])