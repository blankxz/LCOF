class Solution:
    def findNumberIn2DArray(self, matrix, target) -> bool: # O(nm)
        for i in matrix:
            if target in i:
                return True
        return False
    def findNumberIn2DArray2(self, matrix, target) -> bool: # O(n+m)
        row = 0
        if len(matrix) == 0:
            return False
        col = len(matrix[0])-1
        col = len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                col -= 1
            else:
                row += 1
        return False
    def findNumberIn2DArray3(self, matrix, target) -> bool: # O(n+m)
        row = len(matrix)
        if len(matrix) == 0:
            return False
        def find(row_,col_,target,matrix):
            if row_ >= row or col_ < 0:
                return False
            elif target == matrix[row_][col_]:
                return True
            elif target < matrix[row_][col_]:
                return find(row_,col_-1,target,matrix)
            else:
                return find(row_+1,col_,target,matrix)
        return find(0,len(matrix[0])-1,target,matrix)  
        
        

s = Solution()
print(s.findNumberIn2DArray2([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],5))