n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    target,where,how=map(int,input().split()) #target:행 위치, where:방향, how:얼마나 이동
    if where==0:
        for _ in range(how):
            a[target-1].append(a[target-1].pop(0)) #pop(0)은 0번 인덱스 값 제거, 땡긴다.
    else:
        for _ in range(how):
            a[target-1].insert(0, a[target-1].pop()) #insert(0, 넣을 값) 0번 인덱스에 값 추가. pop()은 맨 마지막 제거
# 이후 사과나무 풀이랑 동일
s=0
e=n-1
res=0
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
