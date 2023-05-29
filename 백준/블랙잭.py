# N개 중 3개를 뽑는 조합으로 수를 뽑아 합산
# 그 중 M과 가장 근접한 합을 구한다.

N, M = map(int, input().split())
cards = list(map(int, input().split()))

sum_list = []
choose = []

def combination(index, level):
    if level == 3:
        sum_list.append(sum(choose))
        return
    
    for i in range(index, N):
        choose.append(cards[i])
        combination(i + 1, level + 1)
        choose.pop()
    
combination(0, 0)

target = min([M - x for x in sum_list if M - x >= 0])

print(M - target)