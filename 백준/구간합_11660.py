import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# 누적합 리스트 생성
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + board[i-1][j-1] # board는 0번 인덱스부터 시작하므로

# (x1,y1), (x2,y2) 크기의 합계 계산 (x2 > x1, y2 > y1일 때)
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(result)
