s = input()
dic = {'0','1','2','3','4','5','6','7','8','9'}
data = []
for i in s:
    if i in dic:
        data.append(int(i))
data.sort()
data = [str(i) for i in data]
print(''.join(data))