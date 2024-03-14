# N = 100
# 풀이법: 점수 계산 O(N) + 점수 정렬 O(NlogN)
# 시간복잡도 = O(N) + O(NlogN)
# 시간복잡도 계산 = 100 + 100 * 7 = 800

n = int(input())
lst = []
for _ in range(n):
    b, p, q, r = map(int, input().split())
    lst.append([b, p * q * r, p + q + r]) 

res = sorted(lst, key=lambda x: (x[1], x[2], x[0]))

for x in res[:3]:
    print(x[0], end=' ')