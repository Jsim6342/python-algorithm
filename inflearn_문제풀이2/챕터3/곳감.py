N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

# rotate
for i in range(M):
    row, direction, count = map(int, input().split())

    new_list = [0] * N
    for _ in range(count):
        if direction == 0:
            board[row - 1].append(board[row - 1].pop(0))
        else:
            board[row - 1].insert(0, board[row - 1].pop())


# return
total = 0
start = 0
end = N
for i in range(N):
    for j in range(start, end):
        total += board[i][j]
    if i >= N // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1


print(total)
