import sys

a, b = map(int, sys.stdin.readline().split())

GCD = 0
ab = a * b

while True:
    temp = a % b
    a = b
    b = temp
    if b == 0:
        GCD = a
        break

result = ab // GCD

print(result)