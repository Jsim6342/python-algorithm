# 증가 수열이 꼭 일정 비율로 증가하지 않아도 되구나...
n = int(input())
a = list(map(int,input().split()))

lt = 0
rt = n-1
last = 0 #마지막으로 넣은 값

res = "" #LR 문자열 누적
tmp = []

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort() # 낮은 값을 먼저 넣어야 하므로
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1] == 'L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)