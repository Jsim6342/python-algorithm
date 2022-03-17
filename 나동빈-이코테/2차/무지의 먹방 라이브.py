import heapq


def solution(food_times, k):
    
    # 전체 음식을 먹는 시간 보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    
    food_times = [[val, idx + 1] for idx, val in enumerate(food_times)]
    heapq.heapify(food_times)

    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    while sum_value + ((food_times[0][0] - previous) * length) <= k :
        
        low_food = heapq.heappop(food_times)[0]
        sum_value += length * (low_food - previous)
        length -= 1
        previous = low_food
        

    result = sorted(food_times, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))