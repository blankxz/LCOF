class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return 1*(n-1)
        else:
            if n%3 == 0:
                return 3 ** (n//3)
            elif n%3 == 1:
                return (3 ** (n//3-1)) * 4
            else:
                return  (3 ** (n//3)) * 2

s = Solution()
a = s.cuttingRope(6)
    
print(a)
# 输出
