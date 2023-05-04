N = int(input())
board = []
for _ in range(N):
    now_list = list(map(int, input().split()))
    board.append(now_list)

sum_list = []
for i in range(N):
    row_sum = 0
    col_sum = 0
    for j in range(N):
        row_sum += board[i][j]
        col_sum += board[j][i]
    sum_list.append(row_sum)
    sum_list.append(col_sum)

cross_sum_1 = 0
cross_sum_2 = 0
for i in range(N):
    cross_sum_1 += board[i][i]
    cross_sum_2 += board[N - 1 - i][i]
sum_list.append(cross_sum_1)
sum_list.append(cross_sum_2)

print(max(sum_list))
