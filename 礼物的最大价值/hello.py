class Solution:
    def maxValue(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        db = [0]*len(grid[0])
        db = [db]*len(grid)
        db[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j!=0:
                    db[i][j] = db[i][j-1]+grid[i][j]
                elif i!=0 and j == 0:
                    db[i][j] = db[i-1][j]+grid[i][j]
                else:
                    db[i][j] = max(db[i-1][j],db[i][j-1])+grid[i][j]
        return db[-1][-1]
        
    def maxValue2(self, grid) -> int:
        if not grid:
            return 0
        m = len(grid) -1
        n = len(grid[0])-1
        nums = []
        def dfs(i,j,num):
            if i==m and j==n:
                nums.append(num+grid[i][j])
                return
            elif i<m and j<n:
                dfs(i+1,j,num+grid[i][j])
                dfs(i,j+1,num+grid[i][j])
            elif i==m and j<n:
                dfs(i,j+1,num+grid[i][j])
            elif i<m and j==n:
                dfs(i+1,j,num+grid[i][j])
        dfs(0,0,0)
        return max(nums)
        
s = Solution()
a = s.maxValue([[1,2,5],[3,2,1]])

print(a)