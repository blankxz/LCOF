class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            if dic[i]==1:
                return i
        return ' '
    
a = ['','']

print(a)