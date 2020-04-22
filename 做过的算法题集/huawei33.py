
def judge(nums, k):
    if k == 1:
        return [], sum(nums)
    l = len(nums)
    s = sum(nums)
    if nums[-1] >= s / k:
        sp, val = judge(nums[:-1], k - 1)
        return sp + [l - 1],val
    else:
        i = l
        t = 0
        while t < s / k:
            i -= 1
            t += nums[i]
        sp, val = judge(nums[:i], k - 1)
        maxn = val
        maxsp = sp
        t -= nums[i]
        i += 1
        sp, val = judge(nums[:i], k - 1)
        while t > val and i < n-1:
            maxn = val
            maxsp = sp
            t -= nums[i]
            i += 1
            sp, val = judge(nums[:i], k - 1)
        if t >= maxn:
            maxn = t
            maxsp = sp+[i]
        else:
            maxsp=maxsp+[i-1]
        return maxsp, maxn


m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
sp,val=judge(nums,k)
nums=list(map(str,nums))
n=len(sp)
for i in range(n-1,-1,-1):
    nums.insert(sp[i],'/')
print(' '.join(nums))