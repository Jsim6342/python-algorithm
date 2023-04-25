from collections import deque
n = int(input())
farm = [list(map(int,input().split())) for _ in range(n)]
dq = deque()
std = n//2
sum = 0
for i in range(n):
    if i<=std:
        sum += sum(farm[i][std-i:std+i])
    else:
        sum += sum(farm[i][i-std:i])
print(sum)