n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(0,len(arr)-1):
    if arr[i] > 2*arr[i+1]:
        count+=2
        continue
    if arr[i] > arr[i + 1]:
        if i!=0:
            for j in range(arr[i-1],arr[i+1]):
                t = [arr[i-1],j,arr[i]-j,arr[i+1]]
                tc = t.copy()
                tc.sort()
                if tc == t:
                    count+=1
                    break
        else:
            temp = arr[i+1]
            while temp:
                t = [arr[i]-temp,temp,arr[i+1]]
                tc = t.copy()
                tc.sort()
                if tc == t:
                    count+=1
                    break
                temp -= 1

print(count)