begin = [1,3,0,4,3,5,6,8]
end =   [4,5,6,7,8,9,10,11]
val = [5,1,8,4,6,3,2,4]
pre = [0,0,0,0,0,0,0,0]
for i in range(len(val)):
    if i == 0:
        pre[i] = 0
    else:
        flag = 0
        for j in range(i-1,-1,-1):
            if end[j] <= begin[i]:
                flag = 1
                pre[i] = j+1
                break
        if flag == 0:
            pre[i] = 0

opt = [0]*(len(val)+1)        
for i in range(1,len(val)+1):
    opt[i] = max(opt[i-1],val[i-1]+opt[pre[i-1]])

for i in range(len(val)+1):
    print(opt[i])
