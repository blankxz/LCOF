class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        half = len(nums)//2
        for i in dic:
            if dic[i]>half:
                return i
        # 
