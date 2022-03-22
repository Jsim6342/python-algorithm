import copy

def solution(key, lock):
    answer = False
    N = len(key)
    M = len(lock)
    pre_rotate_key = copy.deepcopy(key)
    
    # Lock 초기화
    # 3M * 3M 크기의 배열을 만들고 Lock을 중앙에 위치시킨다.
    board = [[0] * 3 * M for _ in range(3 * M)]
    for i in range(M,2*M):
        for j in range(M,2*M):
            board[i][j] = lock[i-M][j-M]
    
    for _ in range(4):
        # 90도 회전 구현
        rotate_key = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N-1, -1, -1):
                rotate_key[i].append(pre_rotate_key[j][i]) 

        # 상,하,좌,우 이동 구현
        # board (0,0)부터 key를 탐색시키며, Lock과 정확히 일치하는 지점이 있는지 확인
        for i in range(1, 3*M-N):
            for j in range(1, 3*M-N):
                
                # key 위치
                for y in range(i, N + i):
                    for x in range(j, N + j):
                        board[y][x] += rotate_key[y-i][x-j]
                
                # 일치하는 지점인지 확인
                flag = True
                for y in range(M,2*M):
                    for x in range(M,2*M):
                        if board[y][x] == 0 or board[y][x] > 1:
                            flag = False
                            break
                if flag: return True

                # key 초기화
                for y in range(i, N + i):
                    for x in range(j, N + j):
                        board[y][x] -= rotate_key[y-i][x-j]
        
        # 현재 회전 key 갱신
        pre_rotate_key = copy.deepcopy(rotate_key)
    
    return answer

if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock =[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))