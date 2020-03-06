class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0 : 
            return 0
        if n < 0:
            x , n = 1/x, -n
        res = 1
        while n:
            res *= x if n&1 else 1
            x *= x
            n >>= 1
        return res
    
s = Solution()
a = s.myPow(2,10)
    
print(a)