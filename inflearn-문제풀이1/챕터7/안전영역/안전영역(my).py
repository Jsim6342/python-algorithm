import sys
sys.setrecursionlimit(10**6) #재귀함수 이용 시 타임 리밋을 기입해줘야 한다. (그래야 채점이 된다.)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, h):
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] > h and ch[xx][yy] == 0:
            ch[xx][yy] = 1
            DFS(xx,yy,h)


if __name__=="__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]

    maxNum = -2147000000
    for x in board:
        if max(x)>maxNum:
            maxNum = max(x)

    res = [0] * 101
    cnt= 0
    for h in range(maxNum):
        for i in range(n):
            for j in range(n):
                if board[i][j] > h and ch[i][j] == 0:
                    ch[i][j] = 1
                    DFS(i,j,h)
                    cnt+=1
        res[h] = cnt
        ch = [[0]*n for _ in range(n)]
        cnt = 0
    print(max(res))
