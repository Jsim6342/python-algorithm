import sys
from collections import deque

# board 초기화
n = int(sys.stdin.readline())
board = [[0] * n for _ in range(n)]

# apple 정보 초기화
k = int(sys.stdin.readline())
for _ in range(k):
    y, x = map(int, sys.stdin.readline().split())
    board[y-1][x-1] = 1

DIRS = [[0,1],[-1,0],[0,-1],[1,0]]
moves = deque()
l = int(sys.stdin.readline())
for _ in range(l):
    t, d = sys.stdin.readline().split()
    moves.append([int(t), d])

# 뱀 정보
snake = deque([[0,0]])

time = 0
now_dir = 0
while True:

    
    # 방향 정보 읽기
    if moves and moves[0][0] == time:
        t, d = moves.popleft()
        if d == 'L':
            now_dir = (now_dir + 1) % 4

        if d == 'D':
            now_dir = (now_dir - 1) % 4


    print(time, now_dir)
    
    # 다음 경로 탐색(사과 or 벽인지)
    ny = snake[0][0] + DIRS[now_dir][0]
    nx = snake[0][1] + DIRS[now_dir][1]

    if not (0 <= ny < n and 0 <= nx < n):
        time += 1
        break

    eat_apple = False
    if board[ny][nx] == 1:
        board[ny][nx] = 0
        eat_apple = True

    if [ny,nx] in snake:
        time += 1
        break

    snake.appendleft([ny, nx])
    if not eat_apple:
        snake.pop()

    time += 1
    print(snake)

print(time)