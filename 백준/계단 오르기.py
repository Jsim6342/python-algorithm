# 각 지점마다 최댓값을 저장해 나가는 방식으로 바텀업

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * N

if len(stairs) <= 2:
    print(sum(stairs))
else: 
    dp[0] = stairs[0]
    dp[1] = max(stairs[0]+stairs[1], stairs[1])
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[-1])