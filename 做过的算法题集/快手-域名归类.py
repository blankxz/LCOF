k = int(input())
data = []
for i in range(k):
    data.append(input())
url = []
path = []
for i in data:
    url.append(i.split('/')[:3])
    path.append(i.split('/')[3:])
res = {}
for i in range(k):
    url_ = '/'.join(url[i])
    path_ = '/'.join(path[i])
    if not url_ in res:
        res[url_] = [path_]
    else:
        res[url_].append(path_)
dic2 = {}
for i in res:
    res[i] = list(set(res[i]))
    res[i].sort()
    dic2[''.join(res[i])] = i
paths = []
for i in res:
    if res[i] not in paths:
        paths.append(res[i])
r = []
for i in paths:
    rr = []
    ssss = ''.join(i)
    if ssss in dic2 and ssss!='':
        rr.append(dic2[ssss])
    r.append(rr)
res = []
for i in r:
    if len(i)>1:
        res.append(i)
print(len(res))
for i in res:
    print(' '.join(i))