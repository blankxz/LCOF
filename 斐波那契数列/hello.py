class Solution:
    def __init__(self):
        self.dic = {}
        self.dic[0] = 0
        self.dic[1] = 1
        
    def f(self, n: int) -> int:
        if n in self.dic:
            return self.dic[n]
        else:
            self.dic[n] = self.f(n-1) + self.f(n-2)
            return self.dic[n]
    
    def fib(self, n: int) -> int:
        a = self.f(n)
        return a % (10**9+7)
s = Solution()
a = s.fib(5)

print(a)