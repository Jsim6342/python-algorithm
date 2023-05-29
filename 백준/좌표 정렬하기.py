N = int(input())
dots = []

for _ in range(N):
    dots.append(list(map(int, input().split())))

dots.sort(key=lambda x: (x[0], x[1]))

for x in dots:
    print(*x)