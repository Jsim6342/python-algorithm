INF = 1e9

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

count_list = [0] * (n + 1)

for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        if graph[a][b] == 1:
            count += 1
        if graph[b][a] == 1:
            count += 1
    count_list[a] = count

answer = 0
for i in range(1, n + 1):
    if count_list[i] >= n - 2:
        answer += 1

print(answer)
