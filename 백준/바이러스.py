from collections import deque

N = int(input())
V = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(V):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (N + 1)

# DFS 풀이
def DFS(node):
    if visited[node] == True:
        return

    visited[node] = True

    for next_node in adj_list[node]:
        DFS(next_node)


DFS(1)
print(visited.count(True) - 1)

# BFS 풀이
def BFS(q):
    while q:
        node = q.popleft()
        
        for next_node in adj_list[node]:
            if visited[next_node] == True:
                continue
            q.append(next_node)
            visited[next_node] = True

q = deque()
q.append(1)
visited[1] = True
BFS(q)
print(visited.count(True) - 1)