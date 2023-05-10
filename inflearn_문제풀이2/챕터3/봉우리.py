# init
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

board.insert(0, [0] * N)
board.append([0] * N)
for x in board:
    x.insert(0, 0)
    x.append(0)

# search
count = 0
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if all(board[i][j] > board[i + dir[k][0]][j + dir[k][1]] for k in range(4)):  #all(): 모두가 true일 때 참
            count += 1
print(count)
