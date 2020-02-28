class Solution:
    def replaceSpace(self, s) -> str:
        return s.replace(" ",'%20')
    def replaceSpace2(self, s) -> str:
        return "".join(["%20" if c == " " else c for c in s])

    
s = Solution()
print(s.replaceSpace2("We are happy."))