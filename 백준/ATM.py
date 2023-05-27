N = int(input())
people = list(map(int, input().split()))

people.sort()
result = 0
result_time = []

for time in people:
    result += time
    result_time.append(result)

print(sum(result_time))
