N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
subtraction_numbers = []

for i in range(1, N):
    subtraction_numbers.append(numbers[i] - numbers[i-1])

def GCD(a, b):
    if b == 0: 
        return a
    else:
        return GCD(b, a % b)

gcd = subtraction_numbers[0]
for i in range(1, len(subtraction_numbers)):
    gcd = GCD(gcd, subtraction_numbers[i])

result = set()
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)

print(*sorted(list(result)))
print(*[1,2,3])