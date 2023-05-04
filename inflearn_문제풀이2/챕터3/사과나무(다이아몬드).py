N = int(input())
board = []
for _ in range(N):
    now_list = list(map(int, input().split()))
    board.append(now_list)

sum_result = 0

start = N // 2
end = N // 2
for i in range(N):
    for j in range(start, end + 1):
        sum_result += board[i][j]
    if i < N // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(sum_result)
