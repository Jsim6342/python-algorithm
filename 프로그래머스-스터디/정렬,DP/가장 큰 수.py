
def solution(numbers):
    
    str_numbers = [str(number) for number in numbers]
    sorted_numbers = sorted(str_numbers, key = lambda x: x * 3, reverse = True)
    
    return str(int(''.join(sorted_numbers)))

if __name__ == "__main__":
    numbers = [6, 10, 2]
    print(solution(numbers))