N = int(input())
money_list = [500, 100, 50, 10, 5, 1]
change = 1000 - N
result = 0

for money in money_list:
    if change == 0:
        break
    result += change // money
    change %= money
    
print(result)