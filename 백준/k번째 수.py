# 일반적인 시간초과 풀이
# N = int(input())
# k = int(input())

# A = list([0] * N for _ in range(N))

# B = []

# for i in range(N):
#     for j in range(N):
#         A[i][j] = (i+1) * (j+1)
#         B.append((i+1) * (j+1))

# # print(A)
# (B.sort())
# print(B[k-1])

# 이분탐색을 활용한 풀이
N = int(input())
k = int(input())

start = 1
end = k # N * N이 본래 범위이지만, k를 숫자로 봐도 카운트 시 k의 범위를 넘지 못함
result = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, N+1):
        count += min(mid//i, N)
    
    if count >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)