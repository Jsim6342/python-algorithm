# 시간 복잡도 계산 = 15C7 * N(logN)
from itertools import combinations

L, C = map(int, input().split())
words = list(input().split())
check = ("a", "e", "i", "o", "u")

res = set()
for x in list(combinations(words, L)):
    count = 0
    for check_word in check:
        if check_word in x:
            count += 1
    if count >= 1 and L - count >= 2:
        res.add(''.join(sorted(x)))

pw_list = list(res)
pw_list.sort()
for password in pw_list:
    print(password)
