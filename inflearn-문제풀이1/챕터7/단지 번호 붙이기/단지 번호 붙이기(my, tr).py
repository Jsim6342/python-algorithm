# 주어진 2차 배열 전체를 2중 for문을 돌며 1을 찾는다
# 1이 발견되면, DFS 실행. 지나간 자리는 1로 변환.
# 결과를 res list에 저장
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x,y):
    global cnt
    cnt += 1 # 넘어오자 마자 집 갯수 +1
    board[x][y] = 0
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
            DFS(xx,yy)

if __name__=="__main__":
    n = int(input())
    board = [list(map(int,input())) for _ in range(n)]
    res = [] # 한 단지의 집의 갯수 추가
    for i in range(n):
        for j in range(n):
            if board[i][j]==1: # 집을 발견하면, 그 집의 단지를 탐색
                cnt = 0
                DFS(i,j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)