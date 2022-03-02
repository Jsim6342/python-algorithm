import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향이므로

distance = [INF] * (n + 1)

q = []
distance[1] = 0
heapq.heappush(q, (0, 1))

while q:
    cost, now_node = heapq.heappop(q)
    if cost > distance[now_node]:
        continue
    for next_node in graph[now_node]:
        next_cost = cost + 1
        if next_cost < distance[next_node]:
            distance[next_node] = next_cost
            heapq.heappush(q, (next_cost, next_node))

max_num = -1e9
for i in range(1, n + 1):
    if distance[i] > max_num:
        max_num = distance[i]
        answer_index = i
        count = 1
    elif distance[i] == max_num:
        count += 1

print(answer_index, distance[answer_index], count)
 