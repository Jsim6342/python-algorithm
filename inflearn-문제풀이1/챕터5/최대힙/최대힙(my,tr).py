# 힙은 기본적으로 최소힙으로 작동한다.
# 최대힙을 만들기 위해서는 입력 시 부호를 바꿔서 입력한다.
import heapq as hq
a = [] #힙을 받아줄 리스트 선언
while True:
    num = int(input())
    if num==-1:
        break
    if num==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a)) # 출력할 때 -로 +만들어주기
    else:
        hq.heappop(a, -num) # 받을 때 -로 음수 만들어주기