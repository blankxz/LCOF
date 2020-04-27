class Solution:
    def maxK(self,arr,k):
        if not arr:
            return []
        dic = {}
        for i in arr:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        res = sorted(dic,key=lambda j :dic[j],reverse=True)
        return res[:k]

s = Solution()
print(s.maxK([1,1,1,2,2,3],2))