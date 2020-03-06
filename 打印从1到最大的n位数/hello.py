class Solution:
    def printNumbers(self, n: int):
        return list(range(1,10**n))
    
s = Solution()
a = s.printNumbers(1)
    
print(a)