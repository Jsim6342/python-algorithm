import heapq

INF = 1e9
N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

distance = [INF] * (N + 1)

q = []
heapq.heappush(q, [0, C])
distance[C] = 0

while q:
    now_cost, city = heapq.heappop(q)
    if distance[city] < now_cost:
        continue
    for next_city in graph[city]:
        next_cost = now_cost + next_city[1]
        if distance[next_city[0]] > next_cost:
            distance[next_city[0]] = next_cost
            heapq.heappush(q, [next_cost, next_city[0]])

count = 0
max_distance = 0
for d in distance:
    if d != INF and d != 0:
        count += 1
        max_distance = max(max_distance, d)

print(count, max_distance)