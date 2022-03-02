n = int(input())
a=[list(map(int,input().split())) for _ in range(n)] #for문을 뒤에 쓰면 앞에 문장을 n번 시행

largest=0
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += a[i][j] #행 합
        if sum1>largest:
            largest=sum1
        sum2 += a[j][i]
        if sum2>largest: #열 합
            largest=sum2

#대각선 합
sum1=sum2=0
for i in range(n):
    sum1 += a[i][i]
    if sum1>largest: 
        largest=sum1
    sum2 += a[i][n-i-1]
    if sum1>largest: 
        largest=sum2

print(largest)