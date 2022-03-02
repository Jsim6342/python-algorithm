def Count(len):
    cnt=0 #자르는 토막 갯수
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n = map(int, input().split())
Line=[]
res=0
largest=0

for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp) #기존 값과 비교하여 큰 값을 갱신.
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2 #mid: 1개의 랜선의 길이
    if Count(mid)>=n: #Count() 답이 되는지 안되는지 판단하는 함수
        res=mid
        lt=mid+1
    else: #길이가 길 경우. 긴 쪽은 버려야 된다.
        rt=mid-1
print(res)
