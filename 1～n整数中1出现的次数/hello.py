class Solution:
    def countDigitOne(self, n: int) -> int:
        num = 0
        for i in range(1,n+1):
            for j in str(i):
                if j == '1':
                # print(i)
                    num += 1算是
        print(num)


s = Solution()
a = s.countDigitOne(824883294)

print(a)
