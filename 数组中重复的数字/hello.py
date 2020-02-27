class Solution:
    def findRepeatNumber(self, nums) -> int: # 时间O(nlogn) 空间O(1)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            
    def findRepeatNumber2(self, nums) -> int: # 时间O(n) 空间O(n)
        a = {}
        for i in nums:
            if not i in a:
                a[i] = 1
            else:
                a[i] += 1
        for i in a:
            if not a[i] == 1:
                return i
            
    def findRepeatNumber3(self, nums) -> int: # 时间O(n) 空间O(1)
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] =  nums[i],nums[nums[i]]
s = Solution()
print(s.findRepeatNumber3([0,1 ,3,2,7,5,6,8,8,9,10]))