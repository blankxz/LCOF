import sys

if __name__ == "__main__":
    valueGet = []
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        valueGet.append(values)
    n = valueGet[0][0]
    m = valueGet[0][1]
    k = valueGet[0][2]
    c = valueGet[1]
    c.sort()
    for i in range(m):
        c = [j+k for j in c]
        a = c.pop()//2
        for j in range(len(c)-1,-1,-1):
            if c[j]<a or j == 0:
                c = c[:j+1]+[a]+c[j+1:]
                break
    print(sum(c))