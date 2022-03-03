from collections import deque

def solution(n, m, image):
    chekced = [[False] * m for _ in range(n)]
    dirs = [[-1,0], [1, 0], [0, -1], [0, 1]]
    result = 0
    
    for i in range(n):
        for j in range(m):
            if not chekced[i][j]:
                color = image[i][j]
                q = deque()
                q.append([i, j])
                while q:
                    y, x = q.popleft()
                    for dy, dx in dirs:
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < n and 0 <= xx < m:
                            if not chekced[yy][xx] and image[yy][xx] == color:
                                chekced[yy][xx] = True
                                q.append([yy, xx])
                result += 1
                
    return result


if __name__ == "__main__":
    n = 2
    m = 3
    image = [[1,2,3],[3,2,1]]
    print(solution(n, m, image))
                    