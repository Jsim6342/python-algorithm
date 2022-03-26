# 기둥 조건 체크
def check_build_pillar(pillars, barrages, x, y):
    return y == 0 or (x, y) in barrages or (x-1, y) in barrages or (x, y-1) in pillars

# 보 조건 체크
def check_build_barrage(pillars, barrages, x, y):
    return (x-1, y) in barrages and (x+1, y) in barrages or (x, y-1) in pillars or (x+1, y-1) in pillars

# 삭제 조건 체크
def check_delete(pillars, barrages, x, y):
    
    for pillar in pillars:
        x, y = pillar
        if not check_build_pillar(pillars, barrages, x, y):
            return False
    for barrage in barrages:
        x, y = barrage
        if not check_build_barrage(pillars, barrages, x, y):
            return False
    
    return True

def solution(n, build_frames):
    answer = [[]]
    
    pillars = set()
    barrages = set()
    
    for build_frame in build_frames:
        x, y, a, b = build_frame
        
        # 생성 작업
        if b == 1:
            if a == 0 and check_build_pillar(pillars, barrages, x, y):
                pillars.add((x,y))
            if a == 1 and check_build_barrage(pillars, barrages, x, y):
                barrages.add((x,y))
        # 삭제 작업
        if b == 0:
            if a == 0: pillars.remove((x,y))
            else: barrages.remove((x,y))
            
            if check_delete(pillars, barrages, x, y):
                continue
            
            if a == 0: pillars.add((x,y))
            else: barrages.add((x,y))
            
    # result 생성 및 정렬
    res_pillars = list([x, y] + [0] for (x,y) in pillars)
    res_barrages = list([x, y] + [1] for (x,y) in barrages)
    
    result = res_pillars + res_barrages
    result.sort(key = lambda x: (x[0], x[1], x[2]))    
    
    return result

if __name__ == "__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    print(result == solution(n, build_frame))