class Solution:
    def moneyPay(self,n):
        gradMoney = {5:30,20:15,50:10,100:9,500:8,1000:7,2000:6,3000:5,4000:4,5000:3,6000:2}
        grad = [5,20,50,100,500,1000,2000,3000,4000,5000,6000]
        gradUser = 0
        for j in range(len(grad)-1,-1,-1):
            if n > grad[j]:
                gradUser = j
                break
        money = 0
        tem = 0
        for i in range(gradUser+1):
            n -= grad[i]
            money += grad[i]*gradMoney[grad[i]]
            tem = i
        if not tem > len(grad):
            if n >0 :
                money += n*gradMoney[grad[tem+1]]
        else:
            if n >0 :
                money += n*1
        return money


s = Solution()
print(s.moneyPay(6))