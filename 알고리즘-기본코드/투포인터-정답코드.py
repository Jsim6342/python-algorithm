# 주어진 리스트에서 부분합 M을 만족하는 lt ~ rt 지점 카운트

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = 10
N = len(array)

count = 0
now_sum = 0
rt = 0

for lt in range(N):
    if lt != 0:
        now_sum -= array[lt - 1]
    
    while rt < N and (now_sum + array[rt]) <= M:
        now_sum += array[rt]
        rt += 1
    
    if now_sum == M:
        count += 1

print(count)