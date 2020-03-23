class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*n
        dp[0] = 1
        p2,p3,p5 = 0,0,0
        for i in range(1,n):
            dp[i] = min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
            if dp[i] == dp[p2]*2: p2 += 1
            if dp[i] == dp[p3]*3: p3 += 1
            if dp[i] == dp[p5]*5: p5 += 1 
        return dp[n-1]
        
s = Solution()
a = s.nthUglyNumber(10)

print(a)