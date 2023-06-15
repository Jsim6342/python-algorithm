# 1 ~ 10까지 5개의 수를 조합 뽑기 전체 리스트 출력

# 직접 구현
N = 10
R = 5

array = [i for i in range(N + 1)]
choose = []

def combination(index, level):
    if level == R:
        print(choose)
        return
    
    for i in range(index, N + 1):
        choose.append(array[i])
        combination(i + 1, level + 1)
        choose.pop()

combination(1, 0)

# 함수 활용
from itertools import combinations, combinations_with_replacement

print("===========================")
print(list(combinations(array[1:], 5)))
print("===========================")
print(list(combinations_with_replacement(array[1:], 5)))