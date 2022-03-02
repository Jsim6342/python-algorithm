n, m = map(int, input().split())
weight = list(map(int,input().split()))

sum=0
cnt=0
weight.sort()
for i in range(n):
    if m>sum+weight[i]:
        sum+=weight[i]
    else:
        sum=0
        sum+=weight[i]
        cnt+=1
print(cnt)

# 내 방법이 틀렸다!