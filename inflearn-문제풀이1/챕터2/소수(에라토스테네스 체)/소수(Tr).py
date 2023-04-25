# 소수를 구하는 가장 빠른 방법. 에라토스테네스 체를 활용
# 소수인지 아닌지 판단과 동시에 배수를 제외시킴

n = int(input())

ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)