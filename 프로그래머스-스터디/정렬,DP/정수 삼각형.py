def solution(triangle):
    
    # 양변 각각 +1 크기의 DP 테이블 생성
    DP_triangle = [[0] + triangle[i] + [0] for i in range(len(triangle))]

    # 각 원소에 최댓값을 저장
    # 해당 원소에 접근할 수 있는 경우의 수가 위에서의 좌, 우 최대값에서 오는 경우 밖에 없다는 점을 활용하여 점화식 작성
    # 점화식 = f(x) = max(기존 값 + 윗 변의 왼쪽값, 기존 값 + 윗 변의 오른쪽값)
    for i in range(1, len(DP_triangle)):
        for j in range(1, i + 2):
            DP_triangle[i][j] += max(DP_triangle[i-1][j-1], DP_triangle[i-1][j])
            
    return max(DP_triangle[-1])

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))