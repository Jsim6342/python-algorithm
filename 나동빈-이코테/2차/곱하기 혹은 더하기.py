s = input()

answer = 0

for number in s:
    int_number = int(number)
    if int_number == 0 or answer == 0:
        answer += int_number
    else:
        answer *= int_number

print(answer)    