N = int(input())
horror_points = list(map(int, input().split()))

answer = 0

horror_points.sort()

count = 0
max_number = 0
for horror_point in horror_points:
    max_number = max(max_number, horror_point)
    count += 1
    if max_number == count:
        answer += 1
        count = 0
        max_number = 0

print(answer)