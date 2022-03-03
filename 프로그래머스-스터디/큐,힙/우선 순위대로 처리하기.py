import heapq
from collections import deque

def solution(reqs):
    answer = []
    
    # reqs를 가공하기 쉬운 형태로 변형
    reqs = deque([[-p, t]+ [i + 1] for i, [p, t] in enumerate(reqs)])

    
    now_time = 0
    process_time = 0
    process = []
    while True:
				# reqs와 process가 모두 비면 요청이 마무리 된 것으로 종료
        if len(process) == 0 and len(reqs) == 0: break

				# 3의 배수 시간에는 요청을 process에 추가
        if now_time % 3 == 0 and reqs:
            heapq.heappush(process, reqs.popleft())

				# 프로세스를 모두 수행하면 다른 프로세스를 수행하고 answer에 추가
        if process_time <= 0 and process:
            priority, process_time, index = heapq.heappop(process)
            answer.append(index)
        
        now_time += 1
        process_time -= 1
            
    return answer

if __name__ == "__main__":
    reqs = [[1, 7], [4, 1], [5, 2], [3, 1], [7, 2]]
    print(solution(reqs))