n = int(input())
m = int(input())


graph = [[1e9] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], cost)
    

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(n):
    for b in range(n):
        if graph[a][b] == 1e9:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()