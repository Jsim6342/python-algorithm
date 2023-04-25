from collections import deque

n, k = map(int, input().split())
dq = list(range(1,n+1)) # 1~n까지 한 번에 넣는 방법
dq = deque(dq) # list를 deque로 바꾸는 방법


while dq:
    for _ in range(k-1): #k번째 전 사람은 앞에서 빼서 뒤에 붙인다.
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft() # k번째 사람은 그냥 빼버린다.
    if len(dq)==1: # dq가 1개 남아있으면 프린트
        print(dq[0])
        dq.popleft()