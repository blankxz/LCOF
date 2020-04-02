n, x = list(map(int,input().split( )))
a = list(map(int,input().split( )))

min_ = min(a)
l = len(a)
i = 0
t = 0
while x>=min_:
    if x>=a[i]:
        t += 1
        x-=a[i]
    i+=1
    if i==l:
        i=0
print(t)