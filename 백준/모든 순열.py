# from itertools import permutations

# N = int(input())
# numbers = [x for x in range(1, N+1)]

# result = list(permutations(numbers, N))
# result.sort()

# for x in result:
#     print(*x)
import copy

N = int(input())
numbers = [x for x in range(1, N+1)]
check = [False] * N
choose = []
result = []

def permutation(level):
    if level == N:
        result.append(copy.deepcopy(choose))
        return

    for i in range(N):
        if check[i] == False:       
            choose.append(numbers[i])
            check[i] = True
            permutation(level+1)
            choose.pop()
            check[i] = False

permutation(0)
result.sort()

for x in result:
    print(*x)
