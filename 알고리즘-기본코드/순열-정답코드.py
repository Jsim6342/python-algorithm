# 1 ~ 10까지 3개의 수를 순열 뽑기 전체 리스트 출력

# 직접 구현
N = 10
R = 3

array = [i for i in range(N + 1)]
choose = []
checked = [False] * (N + 1)

def permutation(level):
    if level == R:
        print(choose)
        return
    
    for i in range(1, N + 1):
        if checked[i] == True:
            continue
        choose.append(array[i])
        checked[i] = True
        permutation(level + 1)
        choose.pop()
        checked[i] = False

permutation(0)

# 함수 활용
from itertools import permutations, product

print(list(permutations(array[1:], 3)))
print(list(product(array[1:], repeat=3)))
