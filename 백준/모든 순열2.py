# 시간 복잡도 계산 = 8!

from itertools import permutations

N = int(input())

nums = [x for x in range(1, N+1)]
res = sorted(list(permutations(nums, N)))

for x in res:
    print(*x)

