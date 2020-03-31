class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2,n+1):
            ans = (ans+m)%i
        print(ans)

s = Solution()
s.lastRemaining(5,3)

a = [1,2]
print(a[:0])