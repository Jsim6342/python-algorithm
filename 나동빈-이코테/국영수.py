n = int(input())

info = []
for _ in range(n):
    info.append(list(input().split()))

info.sort(key=lambda x: x[0])
info.sort(key=lambda x: int(x[3]), reverse = True)
info.sort(key=lambda x: int(x[2]))
info.sort(key=lambda x: int(x[1]), reverse = True)

for result in info:
    print(result[0])

