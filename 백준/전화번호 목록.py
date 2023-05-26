import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    phone_number =list(sys.stdin.readline().rstrip() for _ in range(n))
    
    phone_number.sort()

    result = "YES"
    for num1, num2 in zip(phone_number, phone_number[1:]):
        if num2.startswith(num1):
            result = "NO"
            break

    print(result)

