import math
word = input()

str_number = ""
for x in word:
    if x.isdigit():
        str_number += x

result = int(str_number)
print(result)

count = 0
for i in range(1, math.floor(math.sqrt((result))) + 1):
    if result % i == 0:
        count += 1

print(count * 2)
