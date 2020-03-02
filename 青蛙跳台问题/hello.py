class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a , b = b, a+b
        return a % (10**9+7)
        
        
s = Solution()
a = s.numWays(44)
print(a)