N = int(input())
numbers = list(map(int, input().split()))

max_number = max(numbers)

check = [1] * (max_number + 1)
check[0], check[1] = 0, 0

for i in range(2, max_number + 1):
    if check[i] == 1:
        number = i + i
        while max_number >= number:
            check[number] = 0
            number += i

count = 0
for number in numbers:
    if check[number] == 1:
        count += 1

print(count)