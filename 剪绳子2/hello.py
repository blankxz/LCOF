class Solution:
    def cuttingRope(self, n: int) -> int:
        a = 0
        if n <= 3:
            a =  1*(n-1)
        else:
            if n%3 == 0:
                a =  3 ** (n//3)
            elif n%3 == 1:
                a =  (3 ** (n//3-1)) * 4
            else:
                a =  (3 ** (n//3)) * 2
        return a % (10**9+7)

s = Solution()
a = s.cuttingRope(6) #
    
print(a)
