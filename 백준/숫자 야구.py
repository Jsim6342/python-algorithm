# N = 100
# 풀이법: 서로 다른 세 자리 숫자를 하나씩 조건에 맞는지 체크
# 시간복잡도 = 9P3 * 100
from itertools import permutations

N = int(input())
questions = [list(map(int, input().split())) for _ in range(N)]


res = 0
nums = permutations(range(1,10), 3)

for num in nums:
    check = True

    for question in questions:
        q_num = str(question[0])
        strike = 0
        ball = 0
        for i in range(3):
            if str(num[i]) == q_num[i]:
                strike += 1
            elif str(num[i]) in q_num:
                ball += 1
        if int(question[1]) != strike or int(question[2]) != ball:
            check = False
            break
    
    if check:
        res += 1

print(res)



                

        
    