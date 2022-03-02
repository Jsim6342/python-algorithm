n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
b = [list(map(int,input().split())) for _ in range(m)]

target=where=how=0
for i in range(m):
    for j in range(m):
        if j==0:   
            target=b[i][j]
        if j==1:
            where=b[i][j]
        if j==2:
            how=b[i][j]
    for z in range(n):
        if where==0:
            a[target][z]
#풀다가 포기..