def check_aliquot(num):
    num_aliquot = []
    for x in range(1, num):
        if num % x == 0:
            if x == 1 or x == 2 or x == 3 or x == 5:
                num_aliquot.append(x)
            else:
                return False
                
n = int(input())

dp = [1]
num = 2
while len(dp) < 1000:
    check = check_aliquot(num)
    if not check:
        continue
    else:
        if 2 in check or 3 in check or 5 in check:
            dp.append(num)
    num += 1
print(dp)