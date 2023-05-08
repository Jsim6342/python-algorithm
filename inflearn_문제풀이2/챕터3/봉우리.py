# init
N = int(input())

board = [[0] * (N + 2) for _ in range(N + 2)]

input_board = [list(map(int, input().split()) for _ in range(N))]

print(board)
print(input_board)

for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] = input_board[i-1][j-1]

# search
count = 0
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(N):
    for j in range(N):
        check = True
        for k in range(4):
            ny, nx = dir[k]
            if board[ny][nx] > board[i][j]:
                check = False
                break
        if check:
            count += 1

print(count)
