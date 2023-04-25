N, K = map(int, input().split())
cards = list(map(int, input().split()))

sum_set = set()

now_sum = 0
for i in range(N):
    now_sum += cards[i]
    for j in range(N):
        if i == j:
            continue
        now_sum += cards[j]
        for k in range(N):
            if i == k or j == k:
                continue
            now_sum += cards[k]
            sum_set.add(now_sum)
            now_sum -= cards[k]
        now_sum -= cards[j]
    now_sum -= cards[i]

result = sorted(sum_set, reverse=True)
print(result[K - 1])
