import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

current_sum = 0
result = 1e9
rt = 0

for lt in range(N):
    if lt != 0:
        current_sum -= arr[lt-1]

    while rt < N and (current_sum + arr[rt]) <= S:
        current_sum += arr[rt]
        rt += 1

    if current_sum == S:
        length = rt - lt
        if result > length:
            result = length
    elif current_sum < S and rt + 1 < N:
        length = rt + 1 - lt
        if result > length:
            result = length

if result == 1e9:
    result = len(arr)

print(result)
