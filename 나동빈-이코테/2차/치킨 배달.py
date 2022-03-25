import sys
import copy
from itertools import combinations

answer = 1e9

n, m = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i+1,j+1])
        if city[i][j] == 2:
            chickens.append([i+1,j+1])

h = len(houses)
c = len(chickens)

# 각 집 마다 각 치킨집 지점의 치킨 거리 저장
distances = [[] for _ in range(h)] 
index = 0
for house in houses:
    for chicken in chickens:
        distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
        distances[index].append(distance)
    index += 1

# 제거 해야할 치킨집 갯수
remove_count = c - m

remove_candidates = list(combinations(range(c), remove_count))


for remove_candidate in remove_candidates:

    copy_distances = copy.deepcopy(distances)

    for distance in copy_distances:
        count = 0 # pop 할 때 마다 index가 하나씩 줄어들기 때문에 count를 빼줌
        for r in remove_candidate:
            distance.pop(r - count) 
            count += 1

    result = 0
    for distance in copy_distances:
        result += min(distance)

    answer = min(answer, result)

print(answer)
