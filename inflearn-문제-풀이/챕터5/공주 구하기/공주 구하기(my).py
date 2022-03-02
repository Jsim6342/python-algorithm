from collections import deque

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(i+1)
a = deque(a)


while a:
    for i in range(k):
        a.append(a.popleft())
print(a)