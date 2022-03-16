from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp_graph = [[] for _ in range(n)]
    temp = deque(map(int, input().split()))
    
    for i in range(n):
        for j in range(m):
            data = temp.popleft()
            temp_graph[i].append(data)

    graph = [[0] * m for _ in range(n + 2)]

    for i in range(n):
        for j in range(m):
            graph[i+1][j] = temp_graph[i][j]

    for i in range(1, m):
        for j in range(1, n + 1):
            graph[j][i] = max(graph[j][i] + graph[j-1][i-1] ,graph[j][i] + graph[j][i-1], graph[j][i] + graph[j+1][i-1])
            
    result = []
    for x in range(1,n+1):
        result.append(graph[x][-1])
    
    print(max(result))