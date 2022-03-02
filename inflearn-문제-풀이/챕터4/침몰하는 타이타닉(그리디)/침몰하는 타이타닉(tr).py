n, limit = map(int, input().split())
p = list(map(int,input().split()))
p.sort()
cnt=0
while p: # p가 비어있으면 멈춘다.
    if len(p)==1: #1명 남았을 때는 비교할 수 없으므로, 
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1
print(cnt)


