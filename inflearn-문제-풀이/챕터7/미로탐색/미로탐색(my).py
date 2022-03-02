from collections import deque

board = [list(map(int, input().split()))for _ in range(7)]
# 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq = deque()
dq.append((0,0))
#ch[0][0] = 1
cnt = 0
while dq:
    tmp = dq.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            if x==6 and y==6:
                cnt += 1
            else:
                dq.append((x,y))
print(cnt)