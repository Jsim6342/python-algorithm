n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열 주변에 0 넣기
b = [0]*(n+2)

for i in range(n):
    a[i].insert(0,0)
    a[i].append(0)
  
a.append(b)
a.insert(0,b)

#봉우리 갯수 구하기
cnt=0
for i in range(n+2):
    for j in range(n+2):
        if i+1<n+2 and i-1>0 and j+1<n+2 and j-1>0:
            x = a[i][j]
            if x>a[i+1][j] and x>a[i-1][j] and x>a[i][j+1] and x>a[i][j-1]:
                cnt+=1
print(cnt)

# 틀렸네요...
 