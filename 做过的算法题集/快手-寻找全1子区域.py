x, y = list(map(int,input().split()))
data = []
for i in range(x):
    data.append(list(map(int,input().split())))
def dfs(arr,n,m,res):
    if n >= x-1 or m >= y-1 or n<=0 or m <=0:
        return
    a = [arr[n+1][m],arr[n-1][m],arr[n][m+1],arr[n][m-1]] # 下，上，右，左
    b = list(set(a))
    c = sorted(a)
    if -1 not in a:
        if len(b) == 1 and b[0] == 0:
            res += [1]
            return
        else:
            if len(b) == 2 and c[2] == 0:
                arr[n][m] = 0
                if a.index(1) == 0:
                    dfs(arr,n+1,m,res)
                if a.index(1) == 1:
                    dfs(arr,n-1,m,res)
                if a.index(1) == 2:
                    dfs(arr,n,m+1,res)
                if a.index(1) == 3:
                    dfs(arr,n,m-1,res)
                arr[n][m] = 1
            else:
                return
    else:
        return

if x<3 or y<3:
    print(0)
else:
    r = []
    for i in range(0,x):
        for j in range(0,y):
            dfs(data,i,j,r)
            if data[i][j] == 1:
                data[i][j] = -1
    print(len(r))

