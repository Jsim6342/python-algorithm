n = int(input())
coin = list(map(int,input().split()))
m = int(input())
dy = [1000]*(m+1)
for i in range(len(coin)):
    for j in range(coin[i],m+1,coin[i]):
        dy[j]=min(dy[j],dy[j-coin[i]]+1)
print(dy[m])