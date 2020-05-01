n, m = list(map(int,input().split()))
dataMap = [[0]*n for i in range(n)]
for i in range(m):
    a = list(map(int,input().split()))
    dataMap[a[0] - 1][a[1] - 1] = 1
    dataMap[a[1] - 1][a[0] - 1] = 1
count = 0.
visited = [0]*n
def dfs(i):
    visited[i] = 1
    global count
    count += 1
    if count == n:
        return
    for j in range(n):
        if dataMap[i][j] == 1 and not visited[j]:
            dfs(j)
dfs(0)
if count!=n:
    print('NO')
else:
    print('YES')