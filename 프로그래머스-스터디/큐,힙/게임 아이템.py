from collections import deque
import heapq

def solution(healths, items):
    
    answer = []
    
    # items 리스트 가공
    items = [[-power, minus_health] + [idx + 1] for idx, [power, minus_health] in enumerate(items)]
    items = deque(sorted(items, key = lambda x: x[1]))

    # healths 오름차순 정렬
    healths.sort()
    
    # healths를 낮은 순으로 빼내어 낄 수 있는 아이템을 heap에 넣고, 가장 높은 공격력의 아이템을 answer에 저장.
    candidate = []
    for health in healths:
        
        while items and health - items[0][1] >= 100:
            heapq.heappush(candidate, items.popleft())
            
        if candidate:
            item = heapq.heappop(candidate)
            answer.append(item[2])
            
    # 아이템 번호 오름차순 정렬
    answer.sort()
    
    return answer

if __name__ == "__main__":
    healths = [200,120,150]
    items = [[30,100],[500,30],[100,400]]
    print(solution(healths, items))