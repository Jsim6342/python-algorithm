n = int(input())

table = [0] * (n + 1)

if n >= 2:
    table[1] = 1
    table[2] = 2

    for i in range(3, n + 1):
        table[i] = (table[i-2] + table[i-1]) % 10007
elif n == 1:
    table[1] = 1

print(table[n])