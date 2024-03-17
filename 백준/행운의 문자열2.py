# 백 트래킹 방법
from collections import Counter

def func(lev):
    global S, chars, cnt, choose, answer

    if lev == len(S):
        answer += 1
        return
    
    for c in chars:
        if cnt[c] == 0:
            continue

        if (not choose) or (choose[-1] != c):
            cnt[c] -= 1
            choose.append(c)
            func(lev+1)
            cnt[c] += 1
            choose.pop()

S = input()
chars = set(S)
cnt = dict(Counter(S))
choose = []
answer = 0

func(0)
print(answer)

