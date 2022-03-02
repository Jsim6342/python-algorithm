a = [list(map(int,input().split())) for _ in range(9)]


res = "YES"
#행,열 체크
for i in range(9):
    line = [0]*10
    row = [0]*10
    for j in range(9):
        idx = a[i][j]
        line[idx] = 1
        idx = a[j][i]
        row[idx] = 1

    if sum(line)!=9:
        res="NO"
    if sum(row)!=9:
        res="NO"

#사각형 체크
for i in range(0,9,3):
    group = [0]*10
    for j in range(0,9,3):
        group[a[i][j]]=1
        group[a[i][j+1]]=1
        group[a[i][j+2]]=1
        group[a[i+1][j]]=1
        group[a[i+1][j+1]]=1
        group[a[i+1][j+2]]=1
        group[a[i+2][j]]=1
        group[a[i+2][j+1]]=1
        group[a[i+2][j+2]]=1

    if sum(line)!=9:
        res="NO"
print(res)


# 뭔가가 하나 틀리긴 했는데.. 80점은 맞음