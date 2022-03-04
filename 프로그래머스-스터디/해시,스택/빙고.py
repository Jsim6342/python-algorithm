def solution(board, nums):
    answer = 0
    N = len(board)
    dictionary = dict()
    
    # dictionary 초기화
    for i in range(N):
        for j in range(N):
            dictionary[board[i][j]] = [i, j]
            
    # check 2차원 리스트 생성(False로 초기화)
    check = [[False] * N for _ in range(N)]
    
    # check에 Ture 표시
    for num in nums:
        i, j = dictionary[num]
        check[i][j] = True
        
    # 가로, 세로 검사 및 대각선 저장
    cross = []
    reverse_cross = []
    for i in range(N):
        if False not in check[i][:]:
            answer += 1
        if False not in [width[i] for width in check]:
            answer += 1
        cross.append(check[i][i])
        reverse_cross.append(check[i][N - i - 1])
        
    # 대각선 검사    
    if False not in cross:
        answer += 1
    if False not in reverse_cross:
        answer += 1
    
    
    return answer

if __name__ == "__main__":
    board = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
    nums = [14,3,2,4,13,1,16,11,5,15]
    print(solution(board, nums))