# 일정한 규칙을 갖는 DP 테이블 100번째 값 구하기
# 1, 2번째 이전 인덱스를 더해서 인덱스를 갱신해 나가는 바텀업 점화식 세우기 

dp = [0] * 100
N = len(dp)

dp[1] = 1
dp[2] = 1

for i in range(2, N):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[N - 1])