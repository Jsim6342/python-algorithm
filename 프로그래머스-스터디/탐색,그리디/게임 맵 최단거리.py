from collections import deque

def solution(maps):
    
    X = len(maps[0])
    Y = len(maps)
    DIRS = [[1,0],[-1,0],[0,1],[0,-1]]
    
    q = deque()
    q.append([0,0])
    while q:
        y, x = q.popleft()
        for dy, dx in DIRS:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < Y and 0 <= nx < X and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append([ny, nx])
    
    if maps[Y-1][X-1] == 1: return -1
    return maps[Y-1][X-1]

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
    print(solution(maps))