class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            if target-nums[i] in nums[:i]:
                return [i,nums[:i].index(target-nums[i])]
            elif target-nums[i] in nums[i+1:]:
                return [i,nums[i+1:].index(target-nums[i])+i+1]

s = Solution()
print(s.twoSum([2, 7, 11, 15],9))