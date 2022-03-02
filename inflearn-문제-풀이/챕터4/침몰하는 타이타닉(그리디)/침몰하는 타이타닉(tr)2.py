# deque 자료구조로 풀어본다.
# deque: list처럼 자료를 넣다 빼어도 자료 전체가 움직이는 비효율적인 연산이 없음.
# 포인터 자체가 자료가 빼고 나갈 때, 자동적으로 그 전, 그 이후 자료를 가르킨다.
from collections import deque
n, limit = map(int, input().split())
p = list(map(int,input().split()))
p.sort()
p=deque(p)
cnt=0
while p: # p가 비어있으면 멈춘다.
    if len(p)==1: #1명 남았을 때는 비교할 수 없으므로, 
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)