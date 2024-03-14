from itertools import combinations, combinations_with_replacement

N, S = map(int, input().split())
arr = list(map(int, input().split()))

res = []
for i in range(1, N+1):
    res += list(map(sum, combinations(arr, i)))

print(res.count(S))