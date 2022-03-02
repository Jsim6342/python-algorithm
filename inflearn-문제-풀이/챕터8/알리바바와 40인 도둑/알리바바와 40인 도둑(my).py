n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = arr[0][0]
for i in range(n):
    for j in range(n):
        if i==0 and j!=0:
            dy[i][j] = dy[i][j-1]+arr[i][j]
        if j==0 and i!=0:
            dy[i][j] = dy[i-1][j]+arr[i][j]

for i in range(1,n):
    for j in range(1,n):
        if dy[i-1][j] < dy[i][j-1]:
            dy[i][j] = dy[i-1][j]+arr[i][j]
        else:
            dy[i][j] = dy[i][j-1]+arr[i][j]
print(dy[n-1][n-1])