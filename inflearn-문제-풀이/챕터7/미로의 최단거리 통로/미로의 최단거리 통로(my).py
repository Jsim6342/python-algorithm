from collections import deque
dx = [-1, 0, 1, 0] #좌상우하 방향
dy = [0, 1, 0, -1]
a = [list(map(int,input().split())) for _ in range(7)] #값 입력
dq = deque()
dq.append((0,0))
dis = 0
while dq:
    for i in range(4):
        tmp = dq.popleft()
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if a[x][y] != 1:
            if x==6 and y==6:
                dis += 1
                break
            dq.append((x,y))
            dis += 1
print(dis)

# 4방향 탐색을 하면서 해당 방향에 해당하는 dis를 저장하기 위해
# 2차원 배열 dis를 선언하여 각각 저장해야 했었다.
# 위의 알고리즘은 탐색 할 때 마다 dis를 +1하는 형태
# 또한, dq에 들어간 값은 현재 4방향 탐색이 이루어지고 있는 기준 지점으로
# 4방향 탐색이 이루어지기 전 반복문 for문 앞에서 popleft가 이루어져야 한다.