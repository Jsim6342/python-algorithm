# 앞의 최대 부분 증가수열과 동일한 문제다.
# 알고리즘은 동일. 문제만 바꿔서 출제됨
# 왼쪽은 오름차순, 오른쪽 입력되는 부분이 증가수열일 때만 교차되지 않고 선이 연결될 수 있음.

n= int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)