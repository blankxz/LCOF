class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        l = len(num)
        if l == 1:
            return 1
        db = [0]*(l)
        db[0] = 1
        db[1] = 1 if num[:2]>'25' else 2
        for i in range(2,l):
            db[i] = db[i-1] + (db[i-2] if num[i-1:i+1] < '26' and num[i-1] != '0' else 0)
        return db[-1]

a = '12258'
print(a[3:5])
s = Solution()
a = s.translateNum(12258)

print(a)