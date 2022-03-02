n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n):
    triangle[i] = [0] + triangle[i] + [0]

for i in range(1, n):
    for j in range(1, i + 2):
        triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])

print(max(triangle[-1]))