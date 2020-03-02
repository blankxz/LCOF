class Solution:
    def minArray(self, numbers) -> int:
        for i in range(len(numbers)-1):
            if numbers[i+1] < numbers[i]:
                return numbers[i+1]
        return numbers[0]
    
    def minArray2(self, numbers) -> int:
        i ,j = 0, len(numbers)-1
        while i < j:
            m = (i+j)//2
            if numbers[m] > numbers[j]:
                i = m+1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]
        
        
        
s = Solution()
a = s.minArray2([2,2,2,2,2])
print(a)