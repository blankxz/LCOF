class Solution:
    def maxSum(self,arr):
        if len(arr) == 1:
            return arr[0]
        res = arr[0]
        sumTem = arr[0]
        for i in range(1,len(arr)):
            if sumTem < 0:
                sumTem = arr[i]
            else:
                sumTem += arr[i]
            if sumTem > res:
                res = sumTem
        return res

s = Solution()
print(s.maxSum([-2,1,-3,4,-1,2,1,-5,4]))