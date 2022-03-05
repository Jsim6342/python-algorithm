from itertools import combinations

# 에라토스테네스 체로 소수 구하는 함수(리스트로 반환)
def sosu(number):
    is_prime = [True] * (number + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    for num in range(2, number + 1):
        if not is_prime[num]:
            continue
        for x in range(num * num, number + 1, num):
            is_prime[x] = False
        
    return [idx for idx, value in enumerate(is_prime) if value == True]
    
def solution(n):    
    candidate = sosu(n)
    # 3개를 뽑는 조합 중 합이 n과 같은 것만 카운트하여 리턴
    return len([data for data in combinations(candidate, 3) if sum(data) == n])


if __name__ == "__main__":
    n = 33
    print(solution(n))