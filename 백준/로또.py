
# from itertools import combinations

# while True:
#     lotto = list(map(int, input().split()))
#     if lotto[0] == 0:
#         break
#     result = list(combinations(lotto[1:], 6))
#     for x in result:
#         print(*x)
#     print()

choose = []
lotto = []

def make_combinations(index, level):
    if level == 6:
        print(*choose)
        return
    
    for i in range(index, len(lotto)):
        choose.append(lotto[i])
        make_combinations(i+1, level+1)
        choose.pop()


while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    make_combinations(1, 0)
    print()