def DFS(x,y):
    if x == 0:
        print(board[0][y])

    else:
        if 0<=x-1<10 and board[x-1,y] == 1:
            ch[x-1,y] = 1
            DFS(x-1,y)
        elif 0<=x+1<10 and board[x+1,y] == 1:
            ch[x+1,y] = 1
            DFS(x+1,y)
        else:
            DFS(x,y-1)


if __name__=="__main__":
    board = [list(map(int,input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9,y)