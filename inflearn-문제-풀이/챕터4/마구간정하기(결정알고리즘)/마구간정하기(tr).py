def count(len): #가장 가까운 두 말의 거리가 주어졌을 때, 배치할 수 있는 말 수
    cnt=1
    ep=line[0] #마지막에 말을 배치한 지점
    for i in range(1, n):
        if line[i]-ep>=len:
            cnt+=1
            ep=line[i]
    return cnt

n, c =map(int, input().split())
line=[]
for _ in range(n):
    tmp=int(input())
    line.append(tmp)
line.sort() # 정렬 필수!!
lt= 1
rt= line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)>=c: #mid: 가장 가까운 두 말의 거리
        res=mid
        lt = mid+1
    else:
        rt = mid-1
print(res)