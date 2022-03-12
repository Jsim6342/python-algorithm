def solution(N, number):
    answer = -1
    DP = []
    
    for count in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * count))
        
        for i in range(count - 1):
            for num1 in DP[i]:
                for num2 in DP[-i-1]:
                    numbers.add(num1 + num2)
                    numbers.add(num1 - num2)
                    numbers.add(num1 * num2)
                    if num2 != 0:
                        numbers.add(num1 // num2)
        
        if number in numbers:
            answer = count
            break
        
        DP.append(numbers)
        
    return answer

if __name__ == "__main__":
    N = 5
    number = 12
    print(solution(N, number))