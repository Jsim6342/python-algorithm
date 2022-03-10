def solution(d, budget):
    d.sort()
    count = 0
    for department in d:
        budget = budget - department
        if budget >= 0:
            count += 1
        else:
            break
    
    return count

if __name__ == "__main__":
    d = [1,3,2,5,4]
    budget = 9
    print(solution(d, budget))