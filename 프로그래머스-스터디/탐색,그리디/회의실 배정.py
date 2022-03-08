def solution(arr):
    answer = 0
    
    arr.sort(key = lambda schedule : (schedule[1], schedule[0]))
    
    previous_end = 0
    for schedule in arr:
        start, end = schedule
        if start >= previous_end:
            answer += 1
            previous_end = end
    
    
    return answer

if __name__ == "__main__":
    arr = [[1,2],[2,4],[2,2]]
    print(solution(arr))