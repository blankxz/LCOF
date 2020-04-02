n, x = list(map(int,input().split( )))
a = list(map(int,input().split( )))

i = 0
flag = 1
while 1:
    min_ = min(a)
    a = [j-min_ for j in a]
    max_ = max(a)
    min_ = min(a)
    if max(a) - min(a) <= x:
        print(i)
        break
    else:
        if max(a)-x>=x-min(a):
            a.pop(a.index(max_))
        else:
            a.pop(a.index(min_))
        i += 1