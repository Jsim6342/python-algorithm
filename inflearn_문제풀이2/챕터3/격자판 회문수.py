board = [list(map(int,input().split())) for _ in range(7)]

count = 0
for i in range(3):
    for j in range(7):
        # 행 비교
        temp = board[j][i:i+5]
        if temp == temp[::-1]:
            count += 1
        # 열 비교
        for k in range(2):
            if board[i+k][j] != board[i+5-1-k][j]:
                break
        else:
            count += 1
print(count)
