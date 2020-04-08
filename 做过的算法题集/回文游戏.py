n = int(input())
while n:
    a = input()
    if len(a) <= 3:
        if a[0] == a[-1]:
            print('Cassidy')
        else:
            print('Eleanore')
    else:
        len1 = len(list(set(a)))
        len2 = len(a)//2
        if len1 < len2 and len(a)%2!=0:
            print('Eleanore')
        else:
            print('Cassidy')
    n -= 1