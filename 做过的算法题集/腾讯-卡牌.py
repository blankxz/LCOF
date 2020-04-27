n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sorted(a) == a:
    print(0)
else:
    if n == 3:
        print(1)