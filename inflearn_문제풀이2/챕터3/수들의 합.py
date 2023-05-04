N, M = map(int, input().split())
list_a = list(map(int, input().split()))

count = 0
for i in range(N - 1):
    now_sum = list_a[i]
    if sum(list_a[i + 1: N]) + now_sum < M: # 시간 복잡도를 줄이기 위함
        continue
    for j in range(i + 1, N): 
        now_sum += list_a[j]
        if now_sum > M: # M 보다 커지면, 다음 i번째로 넘어감
            break
        elif now_sum == M: # M과 같아지면, count + 1
            count += 1
            break

print(count + list_a.count(M))
