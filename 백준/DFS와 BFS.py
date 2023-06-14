from collections import deque

N, M, V = map(int, input().split())
adj_list = list([] for _ in range(N+1))

DFS_visited = [False] * (N+1)
BFS_visited = [False] * (N+1)

DFS_result = []
BFS_result = []

# 인접리스트 초기화
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 각 간선 정렬
for i in range(1, N+1):
    adj_list[i].sort()

# DFS
def DFS(node):
    if DFS_visited[node] == True:
        return
    
    DFS_result.append(node)
    DFS_visited[node] = True

    for next_node in adj_list[node]:
        DFS(next_node)
        
# BFS
def BFS(q):
    while q:
        node = q.popleft()
        BFS_result.append(node)

        for next_node in adj_list[node]:
            if BFS_visited[next_node]:
                continue
            q.append(next_node)
            BFS_visited[next_node] = True

# DFS 수행
DFS(V)
print(*DFS_result)

# BFS 수행
q = deque()
q.append(V)
BFS_visited[V] = True
BFS(q)
print(*BFS_result)