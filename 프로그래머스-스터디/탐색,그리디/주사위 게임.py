def solution(monster, S1, S2, S3):
    
    count = 0
    for number1 in range(1, S1 + 1):
        for number2 in range(1, S2 + 1):
            for number3 in range(1, S3 + 1):
                if number1 + number2 + number3 + 1 not in monster:
                    count += 1
                    
    answer = int((count / (S1 * S2 * S3)) * 1000)  
    return answer

if __name__ == "__main__":
    monster = [4,9,5,8]
    S1 = 2
    S2 = 3
    S3 = 4
    print(solution(monster, S1, S2, S3))