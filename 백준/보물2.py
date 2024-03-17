# 시간 복잡도 = NlogN * 2

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

res = 0
for i in range(N):
    res += a[i] * b[i]
    
print(res)