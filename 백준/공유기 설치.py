import sys
N, C = map(int, sys.stdin.readline().split())
houses = []

for _ in range(N):
    houses.append(int(sys.stdin.readline()))

houses.sort()

lt = 0
rt = houses[-1] - houses[0]
result = 0

while lt <= rt:
    mid = (lt + rt) // 2

    value = houses[0]
    count = 1
    for i in range(1, N):
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1
    if count >= C:
        lt = mid + 1
        result = mid
    else:
        rt = mid - 1

print(result)