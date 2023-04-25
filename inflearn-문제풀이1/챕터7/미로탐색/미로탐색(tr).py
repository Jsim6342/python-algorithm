# 최단거리가 아니고, 경우의 수를 묻는 경우이기 때문에 DFS로 풀어야한다.
# DFS는 한 곳 방향으로 깊게 탐색 후 백 되는 방식
# BFS는 동심원으로 퍼져나가는 형태로 탐색

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt += 1
    else:
        for i in range(4):
            xx= x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy] = 1 #지나온 길은 1로 채운다.
                DFS(xx, yy)
                board[xx][yy] = 0 #지나온 길에 채운 1을 다시 초기화

if __name__=="__main__":
    board = [list(map(int, input().split()))for _ in range(7)]
    cnt = 0
    board[0][0] = 1 #방문을 한 곳은 1로 채운다.
    DFS(0, 0)
    print(cnt)
