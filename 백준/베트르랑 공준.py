
def search_sosu(target_number):
    check = [1] * (target_number + 1)
    check[0], check[1] = 0, 0

    for i in range(2, target_number + 1):
        if check[i] == 1:
            number = i + i
            while target_number >= number:
                check[number] = 0
                number += i
    
    return check

numbers = []
while True:
    n = int(input())
    if n == 0:
        break
    numbers.append(n)

check = search_sosu(max(numbers) * 2)

for number in numbers:
    count = 0
    for i in range(number + 1, number * 2 + 1):
        if check[i] == 1:
            count += 1
    print(count)