def solution(dirs):
    answer = 0
    
    # 이동 좌표를 dictionary로 만들고, 경로를 저장할 memory 리스트를 생성
    move = {'U':[1,0], 'D':[-1,0], 'L':[0,-1], 'R':[0,1]}
    memory = []
    
    # [5,5]를 시작으로 dirs의 명령어에 따라 경로를 탐색하고, memroy에 저장해 나간다.
    # 저장과 동시에 처음간 경로는 answer + 1을 해준다.
    now_position = [5,5]
    for dir in dirs:
        next_position = [now_position[0] + move[dir][0], now_position[1] + move[dir][1]]

        # 11 x 11 내의 경로를 벗어나면 해당 명령어 무시
        if not 0 <= next_position[0] <= 10 or not 0 <= next_position[1] <= 10:
            continue
            
        # 처음 걸어본 경로 저장
        if [now_position, next_position] not in memory:
            memory.append([now_position, next_position])
            memory.append([next_position, now_position])
            answer += 1
            
        now_position = next_position
    
    return answer
            
if __name__ == "__main__":
    dirs = "ULURRDLLU"
    print(solution(dirs))