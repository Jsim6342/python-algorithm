n, m = map(int,input().split())

a = list(map(int, input().split()))

p1=0
sum=0
cnt=0
while p1<n:
    if sum!=m:
        sum=sum+a[p1]
        p1=p1+1
    if sum==m:
        sum=0
        cnt+=1
print(cnt)

# 풀다가 포기...