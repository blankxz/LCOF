class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 0
        while n:
            a += n & 1
            n >>= 1   
        return a

s = Solution()
a = s.hammingWeight(11)
    
print(a)