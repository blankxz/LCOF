class Solution:
    def maxSubArray(self, nums):
        db = [-999]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                db[i] = nums[i]
            else:
                if db[i-1] <0 :
                    db[i] = nums[i]
                else:
                    db[i] = db[i-1] + nums[i]
        return max(db)
    
s = Solution()
a = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

print(a)



def fib(n):
    
    a = 1
    b = 1
    for i in range(n-2):
        b, a = a +b , b
    print(b)
fib(6)    