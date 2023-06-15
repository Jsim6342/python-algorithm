# 1 ~ 120의 수 중에서 소수 판별
import math

N = 120
isPrime = [True] * (N + 1)
isPrime[0] = isPrime[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if isPrime[i] == False:
        continue
    for j in range(i * 2, N + 1, i):
        isPrime[j] = False

print(isPrime)