N, M = map(int, input().split())

count_dic = dict()

# 합 카운트
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i + j in count_dic:
            count_dic[i + j] += 1
        else:
            count_dic[i + j] = 1

# 가장 확률이 높은 합 추출
max_count = max(count_dic.values())
result = list(key for key in count_dic if count_dic[key] == max_count)

# 출력
for x in result:
    print(x, end=' ')
