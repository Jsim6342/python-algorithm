N = int(input())
check_list = list(map(int, input().split()))

score_list = [0] * N

# 채점 결과(check_list)를 순회하며, score_list를 채워나감
now_score = 0
for i in range(N):
    if check_list[i] == 1:
        now_score += 1
        score_list[i] = now_score
    elif check_list[i] == 0:
        now_score = 0
        score_list[i] = 0

# score_list의 합계가 최종 합산 점수
total_score = sum(score_list)
print(total_score)