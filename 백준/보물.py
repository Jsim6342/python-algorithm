# 풀이법: 오름차순, 내림차순 정렬 후 S계산(곱해서 더하기)

N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0
for i in range(N):
    result += a[i] * b[i]

print(result)