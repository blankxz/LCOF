n, m = list(map(int,input().split()))
a = list(map(int,set(input().split(' '))))
b = list(map(int,input().split(' ')))
a.sort(reverse=True)
b.sort(reverse=True)
money = 0
for i in range(len(b)):
    if a and b[i]>=a[0]:
        money += (b[i]-a[0])
        continue
    if a and b[i]<a[0]:
        while a and b[i]<a[0]:
            a.pop(0)
    if not a:
        money += b[i]
    else:
        money += (b[i] - a[0])
print(money)
