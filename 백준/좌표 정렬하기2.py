# N = 100,000
# 시간복잡도 도출: 정렬 알고리즘 사용으로 N(logN)
# 시간복잡도 = N(logN)
# 시간복잡도 계산 = 10만 * 40 = 약 40만

T = int(input())

points = []
for _ in range(T):
    x, y = map(int, input().split())
    points.append([x,y])

answer = sorted(points, key = lambda x: (x[0], x[1]))

for x, y in answer:
    print(x, y)