import math

def search_sosu(target_number):
    check = [1] * (target_number + 1)
    check[0], check[1] = 0, 0

    for i in range(2, int(math.sqrt(target_number)) + 1):
        if check[i] == 1:
            number = i + i
            while target_number >= number:
                check[number] = 0
                number += i
    
    return check

n = int(input())
check = search_sosu(n)

sosu_list = []
for i in range(n + 1):
    if check[i] == 1:
        sosu_list.append(i)


lt = 0
rt = 0
count = 0
target = sum(sosu_list[lt:rt])

while True:
    
    if target == n:
        count += 1
        target -= sosu_list[lt]
        lt += 1
    elif target > n:
        target -= sosu_list[lt]
        lt += 1
    elif target < n:
        if rt + 1 > len(sosu_list):
            break
        target += sosu_list[rt]
        rt += 1

print(count)