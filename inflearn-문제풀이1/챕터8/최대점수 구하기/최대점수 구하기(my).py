# 문제 유형당 1번만 풀어야 한다는 조건을 적용하지 않음.
n, m = map(int,input().split())
dy=[0]*(m+1)
for i in range(n):
    s, t = map(int, input().split())
    for j in range(t,m+1):
        dy[j]=max(dy[j],dy[j-t]+s)
print(dy[m])