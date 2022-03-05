def solution(brown, red):
    
    total = brown + red
    
    # brown + red 값의 약수를 구한다.
    for number in range(1, total // 2):
        
        # 약수 쌍이 발견되면, brown 갯수와 일치하는지 확인 후, 일치하면 리턴
        if total % number == 0:
            another_number = total // number 
            if (number * 2) + (another_number * 2) - 4 == brown:
                return [another_number, number]

if __name__ == "__main__":
    brown = 10
    red = 2
    print(solution(brown, red))