n, m, a, b = list(map(int,input().split()))
if n==m:
    print(0)
elif n>m:
    print((n-m)*min(a,b))
else:
    temp = n
    while temp!=1:
        if m%temp==0:
            break
        temp -= 1
    redBag = n-temp
    surprise = (m // n + 1) * n - m
    print(min(redBag*a,surprise*b))


# a = min(a,b)
# if n>m:
#     print((n-m)*a)
# else:
#     if m//n < m/n:
#         print(a*((m//n+1)*n-m))
#     else:
#         print(0)
