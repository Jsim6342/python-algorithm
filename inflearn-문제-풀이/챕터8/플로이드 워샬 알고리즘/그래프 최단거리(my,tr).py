n, m = map(int, input().split())
dis = [[5000]*(n+1) for _ in range(n+1)] #최대값으로 초기화한 2차원 list 생성
for i in range(1,n+1): # 자기자신값 0
    dis[i][i] = 0
for i in range(m): # 인접행렬 값 초기화
    a, b, c = map(int, input().split())
    dis[a][b] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j]==5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')

