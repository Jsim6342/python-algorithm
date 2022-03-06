import math
def solution(l, v):

    v.sort()
    answer = max(v[0], l - v[-1]) # 0 ~ 첫 가로등, 마지막 가로등 ~ l 거리 조건
    
    # 각 가로등 사이의 거리를 절반으로 나눈 값을 distances에 저장
    distances = [math.ceil((back - front) / 2) for front, back in zip(v[:-1], v[1:])]
    
    # 가장 긴 거리가 정답
    if distances:
        answer = max(answer, max(distances))

    return answer

if __name__ == "__main__":
    l = 15
    v = [15,5,3,7,9,14,0]
    print(solution(l, v))