n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

res=0
s=e=n//2 # 두 지점을 잡고 n의 절반 지점을 기준으로 계산 변화
         # 두 지점을 잡는다는 것과. 절반 지점은 n//2으로 몫을 이용한다는게 포인트
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)