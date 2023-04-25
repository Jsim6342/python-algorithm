# 중심을 맨 처음 큐에다가 놓고 상태트리를 시작.
# 탐색은 기준에서 부터 상하좌우 탐색
# BFS Level 탐색을 하면 마름모 형태로 탐색된다.

from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)] # 체크하기 위한 2차원 list
sum = 0
dq = deque()
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
dq.append((n//2, n//2))
L = 0
while True:
    if L == n//2:
        break
    size=len(dq)
    for i in range(size): #큐의 크기만큼 반복한다.
        tmp = dq.popleft() #큐에 있는 값 하나를 빼고, 그 값을 기준으로 상하좌우 탐색
        for j in range(4):
            x = tmp[0]+dx[j] #tmp[0]은 dq의 x값
            y = tmp[1]+dy[j] #tmp[1[은 dq의 y값] 
            if ch[x][y]==0: #방문을 안했을 때만
                sum += a[x][y]
                ch[x][y] = 1
                dq.append((x,y))

    #ch를 통한 정상 작동 확인
    # print(L, size)
    # for x in ch:
    #     print(x)
    L=L+1
print(sum)