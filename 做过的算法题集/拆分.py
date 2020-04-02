s = input()
k = int(input())
num = 0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if j-i>=k and j-i>2:
            temp = s[i:j]
            half = (j-i)//2
            for m in range(1,half):
                if temp[:m] == temp[-m:]:
                    num+=1
                    break

print(num)