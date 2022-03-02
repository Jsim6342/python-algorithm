
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dq = deque()
dis = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            dq.append((i,j))

while dq:
    tmp = dq.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0<=xx<m and 0<=yy<n and board[xx][yy] == 0:
            board[xx][yy] = 1 # 토마토 익히기
            dis[xx][yy]=dis[tmp[0]][tmp[1]] + 1 #날짜 하루 더해주는 작업
            dq.append((xx,yy))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0: #모두 1로 바꾸었는데 9이 발견된다면, flag=0으로 바꾼다.
            flag=0

result = 0 #최대값 찾기위한 변수
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
