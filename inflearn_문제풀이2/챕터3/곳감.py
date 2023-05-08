N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

# rotate
for i in range(M):
    row, direction, count = map(int, input().split())

    new_list = [0] * N
    for j in range(N):
        if direction == 0:
            index = j - count
            new_list[index] = board[row][j]
        else:
            index = j + count
            if index >= N:
                index -= N
            new_list[index] = board[row][j]
    board[row] = new_list

# return
total = 0
start = 0
end = N
for i in range(N):
    for j in range(start, end):
        total += board[i][j]
    start += 1
    end -= 1
    if i > N//2:
        start -= 1
        end += 1
