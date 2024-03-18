# 조합 시간 복잡도 = O(2^N)
# 순열 시간 복잡도 = O(N!)
# 이 문제는 조합이므로, 2^20 = 약 100만 풀이가능.
from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

res = []
for i in range(1, N+1):
    res += list(map(sum, combinations(arr, i)))

print(res.count(S))