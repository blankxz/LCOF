res = []


def bfs(data, r, res):
    if len(data) < 1:
        res.append(r)
    else:
        for i in range(len(data)):
            if i != 0 and data[i] == data[i - 1]:
                continue
            bfs(data[:i] + data[i + 1:], r + [data[i]], res)
def foo(n):
    data_ = [1]*n + [-1]*n
    res_ = []
    bfs(data_,[],res_)
    num = 0
    for i in res_:
        s = 0
        flag = 0
        for j in i:
            s += j
            if s<0:
                flag = 1
                break
        if flag ==0 :
            num += 1
    res.append(num)
print(res)
