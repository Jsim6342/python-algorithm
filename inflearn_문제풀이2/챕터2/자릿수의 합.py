N = int(input())
number_list = input().split()


def digit_sum(x):
    sum_number = 0
    for num in x:
        sum_number += int(num)
    return sum_number


max_sum = 0
result = 0
for number in number_list:
    sum_result = digit_sum(number)
    if sum_result > max_sum:
        max_sum = sum_result
        result = int(number)

print(result)
