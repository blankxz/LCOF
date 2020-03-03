class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        dfs(38,39,1)
        def dfs(i,j,k):
            s = 0
            a = i
            b = j
            while a:
                s += a%10
                a/=10
            while b:
                s += b%10
                b/=10
            print(s)
                    
            # if not 0<=i<m or not 0<=j<n or 
        
s = Solution()
a = s.movingCount(2,3,1)

print(a)