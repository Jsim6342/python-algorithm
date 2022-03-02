dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==maxIdx[0] and y==maxIdx[1]:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if san[xx][yy] > san[x][y] and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                DFS(xx,yy)
                ch[xx][yy] = 0

if __name__=="__main__":
    n = int(input())
    san = [list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    maxIdx = list()
    minIdx = list()
    for i in range(n):
        for j in range(n):
            if san[i][j] > max:
                max = san[i][j]
                maxIdx.append(i)
                maxIdx.append(j)
            if san[i][j] < min:
                min = san[i][j]
                minIdx.append(i)
                minIdx.append(j)
    cnt = 0
    ch[minIdx[0]][minIdx[1]] = 1
    DFS(minIdx[0],minIdx[1])
    print(cnt)