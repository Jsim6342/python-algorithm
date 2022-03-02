n, m = map(int,input().split())

a = list(map(int, input().split()))

# 알고리즘: 
# lt, rt의 포인터 변수 2개를 둔다
# lt 부터 rt 바로 전 까지 더하여 tot변수에 저장
# tot의 3가지 경우, m보다 작을 때, 같을 때, 클 때로 나눈다
# tot<m일 때, rt를 전진시키며 더함. tot==m일 때, cnt하고 lt 빼고 lt 전진. tot>m일 때, lt 빼고 lt 전진
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break #rt>n일 때 break로 종료
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)
        