# 단지 번호 붙이기 문제와 도일한 문제이다.
# 풀이법은 강사님꺼 보고 혼자서 풀이함
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dq = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt+=1
            board[i][j] = 0
            dq.append((i,j))
            while dq:
                tmp = dq.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y] == 1:
                        board[x][y] = 0;
                        dq.append((x,y))
print(cnt)