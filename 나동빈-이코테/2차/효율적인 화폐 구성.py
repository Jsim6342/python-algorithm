import sys
N, M = map(int, sys.stdin.readline().split())

MAX_NUM = 10001

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

DP = [MAX_NUM] * MAX_NUM
DP[0] = 0

for x in range(1, MAX_NUM):
    for coin in coins:
        if x - coin >= 0:
            DP[x] = min(DP[x], DP[x - coin] + 1)
    if x == M:
        break

if DP[M] == MAX_NUM:
    print(-1)
else:
    print(DP[M])