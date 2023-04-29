# 에라토스테네스의 체 알고리즘으로 소수 개수를 구함

N = int(input())

check = [0] * (N + 1)

for number in range(2, N + 1):
    if check[number] == N:
        continue
    i = 2
    while True:
        if number * i > N:
            break
        check[number * i] = 1
        i += 1
    
result = check.count(0) - 2
print(result)
