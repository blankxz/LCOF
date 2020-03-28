def func(s):
    flag = 0
    s_ = s[0]
    res = ''
    r = []
    for i in s:
        if not i == s_:
            r.append([s_,flag])
            res = res + s_ +str(flag)
            flag = 1
            s_ = i
        else:
            flag += 1
    r.append([s_, flag])
    r.sort(key=lambda a:a[1])
    print(''.join([''.join(list(map(str,i))) for i in r]))
    print(r)
    res = res+s_+str(flag)
    return res

print(func('eeeeeaaaffeee'))
