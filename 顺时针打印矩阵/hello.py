class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        l ,r ,t, b = 0, len(matrix[0])-1, 0, len(matrix) -1
        res = []
        while True:
            for i in range(l,r+1):
                print(matrix[t][i])
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t,b+1):
                print(matrix[i][r])
                res.append(matrix[i][r])
            r -= 1
            if l>r:
                break
            for i in range(r,l-1,-1):
                print(matrix[b][i])
                res.append(matrix[b][i])
            b -= 1
            if t>b:
                break
            for i in range(b,t-1,-1):
                print(matrix[i][l])
                res.append(matrix[i][l])
            l+=1
            if l>r:
                break
        return res
            
s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))



def spiralOrde2r(matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res+=matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res