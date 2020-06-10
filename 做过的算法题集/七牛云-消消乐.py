t = int(input())
for i in range(t):
    s = list(input())
    if len(s) == 1:
        print('No')
        continue
    while 1:
        n = 0
        m = 0
        for j in range(len(s)):
            if len(s[n:m]) == 2:
                for x in range(n, m):1
                    s[x] = '0'
                n = j
                m = n + 1
                continue
            if s[j]!=s[n]:
                n = j
                m = n+1
            else:
                m += 1
            # print(s[n:m])
        if len(s[n:m]) == 2:
            for x in range(n, m):
                s[x] = '0'
        r = []1
        # print(s)11
        for x in s:
            if x != '0':
                r.append(x)
        # print(r)
        # print(s)
        if r == s:
            break
        else:
            s = r
    if not s:
        print('Yes')
    else:
        print('No')
