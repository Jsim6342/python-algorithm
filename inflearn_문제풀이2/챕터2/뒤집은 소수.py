def isPrime(reverse_number):
    if check[reverse_number] == 0:
        return True
    else:
        return False


def reverse(number):
    word_number = []
    for word in number:
        word_number.append(word)
    reverse_number = ""
    for word in word_number[::-1]:
        reverse_number += word
    return reverse_number


N = int(input())
number_list = list(input().split())

reverse_number_list = []
for number in number_list:
    reverse_number_list.append(int(reverse(number)))


# print(reverse_number_list)

max_number = max(reverse_number_list)

# 에라토스테네스 체
check = [0] * (max_number + 1)
check[0] = 1
check[1] = 1

for number in range(2, max_number + 1):
    if check[number] == 1:
        continue
    i = 2
    while True:
        if number * i > max_number:
            break
        check[number * i] = 1
        i += 1

# print(check)

result = []
for reverse_number in reverse_number_list:
    if (isPrime(reverse_number)):
        result.append(reverse_number)

for x in result:
    print(x, end=' ')
