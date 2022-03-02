from collections import deque
dx = [-1, 0, 1, 0] #좌상우하 방향
dy = [0, 1, 0, -1]
board = [list(map(int,input().split())) for _ in range(7)] #값 입력
dis=[[0]*7 for _ in range(7)]
dq = deque()
dq.append((0,0)) #출발점
board[0][0]=1 #한 번 방문한 곳은 1로 채운다.
while dq: # 큐가 비면 멈춘다.
    tmp = dq.popleft()
    for i in range(4):     
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
            board[x][y] = 1 #방문한 곳은 1로 채운다.
            dis[x][y] = dis[tmp[0]][tmp[1]]+1 #거리를 더해간다.
            dq.append((x,y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])