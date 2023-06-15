# a와 b의 최대공약수 구하기
# eX) 21, 14의 최대공약수 구하기

import math

# 함수 활용
print(math.gcd(21, 14))

# 알고리즘 활용
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

print(GCD(21, 14))