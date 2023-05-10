
board = [list(map(int, input().split())) for _ in range(9)]

check_dictionary = dict()
for i in range(1, 10):
    check_dictionary[i] = 0

# row, col
result = "YES"
now_value = 0
for i in range(9):
    for j in range(9):
        check_dictionary[board[i][j]] += 1
        check_dictionary[board[j][i]] += 1
    now_value += 2
    if list(check_dictionary.values()).count(now_value) != 9:
        result = "NO"
        break


# 3x3
for k in range(3):
    for i in range(3):
        for j in range(3):
            check_dictionary[board[i][j]] += 1
    now_value += 1
    if list(check_dictionary.values()).count(now_value) != 9:
        result = "NO"
        break

print(result)
