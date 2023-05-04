N, M = map(int, input().split())
list_a = list(map(int, input().split()))

count = 0
for i in range(N):
    now_sum = 0
    for j in range(i + 1, N):
        now_sum += list_a[j]
        if now_sum > N:
            break
        elif now_sum == N:
            count += 1
    print(now_sum)
print(count)