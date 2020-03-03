class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        mat = [None] * m
        for i in range(m):
            mat[i] = [1]*n
        mm = m
        nn = n
        def dfs(i,j,k):
            s = 0
            a = i
            b = j
            while a>0:
                s += a%10
                a//=10
            while b>0:
                s += b%10
                b//=10
            if not 0<=i<mm or not 0<=j<nn or s > k or mat[i][j] == 0: return 0
            mat[i][j] = 0
            return 1 + dfs(i+1,j,k) + dfs(i,j+1,k) + dfs(i-1,j,k) + dfs(i,j-1,k)
            
        return dfs(0,0,k)
            
        
s = Solution()
a = s.movingCount(2,3,1)
print(a)