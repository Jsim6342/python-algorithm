from collections import deque
n, m = map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1)
dQ=deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    degree[b]+=1
for i in range(1, n+1):
    if degree[i]==0:
        dQ.append(i)
while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1,n+1):
        if graph[x][i]==1: #그래프에서 x로 부터 비롯된 진입차수가 1인 것들의 도착점 i를 찾는다.
            degree[i]-=1 #그 i의 진입차수를 -1하고
            if degree[i]==0: #만약 0이되면 큐에 넣는다.
                dQ.append(i)