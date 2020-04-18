def solution():
    n = int(input())
    for i in range(n):
        data  = []
        for j in range(6):
            data.append(list(map(int,input().split())))
        for j in data:
            j.sort(reverse=True)
        len_ = []
        for j in data:
            len_.append(j[0])
            len_.append(j[1])
        a = len(set(len_))
        b = list(set(len_))
        if a == 1:
            print('POSSIBLE')
        elif a == 2:
            c = {b[0]: 0, b[1]: 0}
            c2 = {b[0]: 0, b[1]: 0}
            for j in b:
                for x in data:
                    if j in x:
                        c[j] += 1
                    for m in x:
                        if m == j:
                            c2[j] += 1
            res = 'IMPOSSIBLE'
            for j in c:
                if c[j] == 4 and c2[j] == 4:
                    res = 'POSSIBLE'
            print(res)

        elif a == 3:
            c = {b[0]:0,b[1]:0,b[2]:0}
            c2 = {b[0]: 0, b[1]: 0, b[2]: 0}
            for j in b:
                for x in data:
                    if j in x:
                        c[j] += 1
                    for m in x:
                        if m == j:
                            c2[j]+=1
            res = 'POSSIBLE'
            for j in c:
                if c[j] != 4 or c2[j]!=4:
                    res = 'IMPOSSIBLE'
            print(res)
        else:
            print('IMPOSSIBLE')
solution()