import math

N, K = map(int, input().split())

result = list()

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        result.append(i)
        if i != N / i:
            result.append(int(N / i))

result.sort()

if (K > len(result)):
    print(-1)
else:
    print(result[K - 1])
