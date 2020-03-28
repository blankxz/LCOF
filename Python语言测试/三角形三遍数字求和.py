import sys

def func(arr,r,res):
    if len(arr) < 1:
        res.append(''.join(r))
    else:
        for i in range(0,len(arr)):
            if i>0 and arr[i]==arr[i-1]:
                continue
            func(arr[:i]+arr[i+1:],r+[arr[i]],res)

for line in sys.stdin:
    nums = line.split(',')
    nums_list = [i.replace('\n','') for i in nums]
    res_ = []
    func(nums_list,[],res_)
    flag = 0
    for i in res_:
        arrNum = list(i)
        a = list(map(int,arrNum[:4]))
        b = list(map(int,arrNum[3:7]))
        c = list(map(int,arrNum[6:]+[arrNum[0]]))
        if sum(a) == sum(b) == sum(c):
            flag = 1
            print('yes')
            break
    if flag == 0:
        print('no')

