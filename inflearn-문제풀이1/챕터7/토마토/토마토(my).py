
dx = [-1, 0, 1, 0]
dy = [9, 1, 0, -1]

def DFS(x,y):
    for i in range(4):
        xx = x + dx[x]
        yy = y + dy[y]
        if 0<=xx<n and 0<=yy<m and board[xx][yy] == 0:
            board[xx][yy] = 1
             

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
while True:

        
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                DFS(i,j)
    cnt += 1

    #마지막 조건인 모두 1로 바뀌었을 때와 모두 익지 못하는 경우 -1을 출력해야하는 조건을 구현 못했다.