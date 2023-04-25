import sys
sys.setrecursionlimit(10**6) #재귀함수 이용 시 타임 리밋을 기입해줘야 한다. (그래야 채점이 된다.)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, h):
    ch[x][y] = 1
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] > h and ch[xx][yy] == 0:
            DFS(xx,yy,h)


if __name__=="__main__":
    n = int(input())
    res = 0
    cnt= 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100): #기존의 단지 번호 붙이기에 높이에 따른 반복 조건이 붙은 문제이다.
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] > h and ch[i][j] == 0:
                    cnt+=1
                    DFS(i,j,h)
            res = max(res, cnt) #기존의 res 보다 cnt가 크다면 res에 넣어라
            if cnt==0: # cnt==0이다는 것은 board 내의 최대 높이임을 의미한다.
                break
    print(res)