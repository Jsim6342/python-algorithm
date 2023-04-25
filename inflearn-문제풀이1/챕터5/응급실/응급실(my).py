from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i,x in enumerate(a):
    b.append([x,i])

dq = deque(b)
save = dq[m]
stack = []

while dq:
    maxval = max(dq)
    if dq[0][0]<maxval[0]:
        n = dq.popleft()
        dq.append(n)
    else:
        n = dq.popleft()
        stack.append(n)

cnt=0
for x in stack:
    if x[1]==m:
        cnt+=1
        break
    cnt+=1

print(cnt)

# 정답!