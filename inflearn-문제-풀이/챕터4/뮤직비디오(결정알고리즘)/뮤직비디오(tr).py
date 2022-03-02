
#내 풀이에서 문제 잘못이해함!!!! -> 최소 용량 DVD m개로 모든 영상을 녹화할 수 있는 m을 구하는 것!

def count(capacity):
    cnt=1
    sum=0
    for x in music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt


n, m = map(int, input().split())
music = list(map(int, input().split()))

maxx = max(music) #dvd 용량의 크기는 최대 크기 용량 보다는 커야한다.

lt = 1
rt = sum(music)
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    if mid>=maxx and count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
