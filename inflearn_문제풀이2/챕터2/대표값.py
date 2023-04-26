N = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / N)

min_gap = 1e9
for score in scores:
    if min_gap >= abs(avg - score):
        min_gap = abs(avg - score)

result_list = []
for index, score in enumerate(scores):
    if min_gap == abs(avg - score):
        result_list.append((index + 1, score))


result_list.sort(key=lambda x: (x[1], -x[0]), reverse=True)

print(avg, result_list[0][0])
