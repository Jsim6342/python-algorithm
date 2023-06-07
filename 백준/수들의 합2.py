import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

result = 0
current_sum = 0
rt = 0
for lt in range(N):
    if lt != 0:
        current_sum -= numbers[lt-1]

    while rt < N and (current_sum + numbers[rt]) <= M:
        current_sum += numbers[rt]
        rt += 1

    if current_sum == M:
        result += 1

print(result)
