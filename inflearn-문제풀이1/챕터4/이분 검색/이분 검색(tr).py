n, m = map(int, input().split())
a = list(map(int, input().split()))

# 이분 검색을 하기 위해선 오름차순, 내림차순 정렬이 선제조건
a.sort()
lt=0
rt=n-1
while lt<=rt: #lt가 rt보다 크거나 같아지면, 탐색이 종료된다.
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1