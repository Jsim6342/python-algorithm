import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while True:
        food1 = heapq.heappop(scoville)
        
        if food1 >= K: return count
        if len(scoville) == 0 and food1 < K: return -1
        
        food2 = heapq.heappop(scoville)
        
        mix_food = food1 + (food2 * 2)
        
        heapq.heappush(scoville, mix_food)
        count += 1
        
    return count

if __name__ == "__main__":
    scoville = [1,2,3,9,10,12]
    K = 7
    print(solution(scoville, K))