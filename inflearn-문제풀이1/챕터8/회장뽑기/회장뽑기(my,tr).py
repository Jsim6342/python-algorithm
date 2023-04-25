n=int(input())
dis=[[100]*(n+1) for _ in range(n+1)]
# 자기자신 0으로 초기화
for i in range(1,n+1):
    dis[i][i]=0
# 입력값 초기화
while True:
    a, b = map(int,input().split())
    if a==-1 and b==-1:
        break
    dis[a][b]=1
    dis[b][a]=1
# 플로이드 와샬 적용
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
# 각 회원의 회원점수를 res에 기입
res=[0]*(n+1)
score=100
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i]=max(res[i],dis[i][j]) #가까움의 정도가 가장 큰 수가 res[i]에 저장. 점수가 가장 큰 걸 기준으로 하나봄..
    score=min(score,res[i])
    out=[] #회장 후보의 list가 저장
for i in range(1, n+1):
    if res[i]==score:
            out.append(i)
print("%d %d" %(score, len(out))) #점수와 후보 학생수 출력
for x in out:
    print(x, end=' ') #학생 번호 출력