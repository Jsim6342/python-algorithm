n = int(input())
dp = [[0] for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = list(map(int, input().split()))

PERIOD, COST = 0, 1

for i in range(1, n+1):

    time = dp[i][PERIOD] + i
    if time <= n:
        dp[time][COST] = max(dp[i][COST] + dp[time][COST], dp[time][COST]) 
    else:
        dp[time][COST] = max(dp[i][COST], dp[time][COST])

print(dp)
            