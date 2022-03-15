def solution(m, n, puddles):

    DP = [[0] * (m+1) for i in range(n+1)]
    # DP 초기값 설정
    DP[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                DP[i][j] = 0
            else:
                DP[i][j] = DP[i-1][j] + DP[i][j-1]      

    return DP[n][m] % 1_000_000_007

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2,2]]
    print(solution(m, n, puddles))