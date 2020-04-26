class Solution:
    def get_max(self , input_array):
        if not input_array:
            return 0
        maxNum = 0
        i = 0
        j = 0
        l = len(input_array)
        s = 0
        while j<l:
            s = s+input_array[j]
            if s>maxNum:
                maxNum = s
            if s<0:
                s = 0
            j += 1
        return maxNum

s = Solution()
print(s.get_max([1,-2,3]))