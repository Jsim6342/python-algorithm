# 노드가 1~5, 간선이 6개인 인접 리스트가 주어짐
# 주어진 인접 리스트를 BFS로 순회
from collections import deque

N = 6
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

adj_list[1].append(2); adj_list[1].append(3)
adj_list[2].append(5); adj_list[2].append(4)
adj_list[3].append(4)
adj_list[4].append(1)

q = deque()
q.append(1)
visited[1] = True

while q:
    node = q.popleft()
    
    print(node, end = ' ')

    for next_node in adj_list[node]:
        if visited[next_node] == True:
            continue
        q.append(next_node)
        visited[next_node] = True


