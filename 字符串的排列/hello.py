class Solution:

    def permutation(self, s: str):
        s = sorted(list(s))
        res = []
        def fuc(s,tmp):
            if s == []:
                res.append(''.join(tmp))
            for i in range(len(s)):
                if i > 0 and s[i] == s[i-1]:
                    continue
                fuc(s[:i]+s[i+1:],tmp+s[i])
        fuc(s,'')
        return  res
    
s = Solution()
print(s.permutation('abbc'))

