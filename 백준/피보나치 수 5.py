# 시간 복잡도: O(N)
# 시간 복잡도 계산 = 20
# 메모이제이션을 하지 않은 재귀는 O(2^N)

def fibo(n):
    global memo

    # base case
    if memo[n] != -1:
        return memo[n]
    
    # recursive case
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())

memo = [-1] * (n + 2)
memo[0] = 0
memo[1] = 1

print(fibo(n))