# 브루트포스 시간 복잡도: 3 * 2^(N-1)로 불가능
# 그리디 풀이: 순간 최선의 선택이 최적해가 아니라 불가능
# dp 풀이: 이전의 선택을 반영하여 각 R,G,B 별 최소값을 갱신 -> 시간 복잡도: O(3N)

N = int(input())
cost = []
cost += [list(map(int, input().split())) for _ in range(N)]

# dp 테이블 세팅 및 초기값 세팅
dp = [[-1, -1, -1] for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))