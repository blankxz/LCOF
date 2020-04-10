'''

param: [[R-RR-],[RS-SS],[RS-SS],[RSS--],[RRSS-]], N, M
return: Matrix map

'''

def draw(matrix,n,m):
    matrixMap = [0] * n
    for i in range(n):
        matrixMap [i] = [0] * m

    print(matrixMap)
    t = 0
    ind = 0
    if n%2==0:
        flag = 0 # 向左
        for i in range(n):
            print(i)
            if i == 0:
                temp = 0
                while temp < m:
                    print(temp)
                    temp += 1
                    t += 1
                    if (t-1)%3==0:
                        matrixMap[i][temp] = matrix[ind][0][0]
                        if i >0:
                            matrixMap[i-1][temp] = matrix[ind][0][1]
                        if temp <m-1:
                            matrixMap[i][temp+1] = matrix[ind][0][1]
                        if i <n-1:
                            matrixMap[i-1][temp] = matrix[ind][0][1]
                        if temp >0:
                            matrixMap[i-1][temp] = matrix[ind][0][1]
                        ind+=1
            else:
                if flag == 0:
                    temp = m
                    while temp>0:
                        temp -= 1
                        t += 1
                        if (t - 1) % 3 == 0:
                            matrixMap[i][temp] = matrix[ind][0][0]
                            if i > 0:
                                matrixMap[i - 1][temp] = matrix[ind][0][1]
                            if temp < m-1:
                                matrixMap[i][temp + 1] = matrix[ind][0][1]
                            if i < n-1:
                                matrixMap[i - 1][temp] = matrix[ind][0][1]
                            if temp > 0:
                                matrixMap[i - 1][temp] = matrix[ind][0][1]
                            ind += 1
                    flag = 1
                if flag == 0:
                    temp = 1
                    while temp<m:
                        temp += 1
                        t += 1
                        if (t - 1) % 3 == 0:
                            matrixMap[i][temp] = matrix[ind][0][0]
                            if i > 0:
                                matrixMap[i - 1][temp] = matrix[ind][0][1]
                            if temp < m:
                                matrixMap[i][temp + 1] = matrix[ind][0][1]
                            if i < n:
                                matrixMap[i - 1][temp] = matrix[ind][0][1]
                            if temp > 0:
                                matrixMap[i - 1][temp] = matrix[ind][0][1]
                            ind += 1
                    flag = 0
        while n>0:
            t+=1
            if (t - 1) % 3 == 0:
                matrixMap[n-1][0] = matrix[ind][0][0]
                ind += 1
            n -= 1
    return matrixMap

print(draw([['R-RR-'],['RS-SS'],['RS-SS'],['SSS--'],['RRSS-']],4,3))