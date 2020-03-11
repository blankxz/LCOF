class Solution:
    def exchange(self, nums):
        if not nums:
            return nums
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] % 2 != 0:
                left += 1
                continue
            if nums[right] % 2 == 0:
                right -= 1
                continue
            nums[left] , nums[right] = nums[right], nums[left]
        return nums
                

s = Solution()
print(s.exchange([1,2,3,4]))