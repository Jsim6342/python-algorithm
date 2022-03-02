import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(m + 1)]

for _ in range(m + 1):
    a, b = map(int, input().split())
    graph[a].append(b)

x, k = map(int, input().split())

INF = 1e9
distance = [INF] * (m + 1)

route = list()
heapq.heappush(route, (0, 1))
distance[1] = 0
while route:
    cost, node = heapq.heappop(route)

    if distance[node] < cost:
        continue
    for next_node in graph[node]:
        next_distance = cost + 1
        if next_distance < distance[next_node]:
            distance[next_node] = next_distance
            heapq.heappush(route, (next_distance, next_node))