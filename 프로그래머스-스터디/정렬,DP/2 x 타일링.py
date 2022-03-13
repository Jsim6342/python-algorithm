def solution(n):
    DP = [0] * (n + 1)
    
    DP[1] = 1
    DP[2] = 2
    for i in range(3, n+1):
        DP[i] = (DP[i-2] + DP[i-1]) % 1_000_000_007
        
    return DP[n] 

if __name__ == "__main__":
    n = 4
    print(solution(n))