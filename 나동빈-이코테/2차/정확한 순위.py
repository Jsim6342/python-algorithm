INF = 1e9

n, m = map(int, input().split())

graph = [[INF] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for a in range(n):
    count = 0
    for b in range(n):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
    if count == n:
        result += 1

print(result)

