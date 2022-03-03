import math

def solution(progresses, speeds):
    result = []
    dates = []
    
    for progress, speed in zip(progresses, speeds):
        dates.append(math.ceil((100 - progress) / speed))
    
    maxNum = dates[0]
    count = 0
    for date in dates:
        if date > maxNum:
            maxNum = date
            result.append(count)
            count = 1
        else:
            count += 1
    result.append(count)
    
    return result

if __name__ == "__main__":
    progresses = [93,90,55]
    speeds = [1,30,5]
    print(solution(progresses, speeds))