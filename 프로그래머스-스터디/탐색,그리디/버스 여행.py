def solution(n,signs):
    answer = []

    # i -> j -> k로 갈 수 있다면, i -> k로도 갈 수 있다.
    # 해당 알고리즘을 한 번만 수행했을 경우에는 갱신되지 않은 루트가 있을 수 있기 때문에 2번 반복
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if signs[i][j] == 1 and signs[j][k] == 1:
                    signs[i][k] = 1
                    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if signs[i][j] == 1 and signs[j][k] == 1:
                    signs[i][k] = 1
    
    
    return signs

if __name__ == "__main__":
    n = 3
    signs = [[0,1,0],[0,0,1],[1,0,0]]
    print(solution(n, signs))