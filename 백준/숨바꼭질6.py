# 풀이 핵심: 내 위치와 동생의 위치를 뺀 차이의 최대공약수가 정답

N, S = map(int, input().split())
spots = list(map(int, input().split()))

dif_spots = [abs(x - S) for x in spots]

def GCD(a, b):
    if b == 0: return a
    else: return GCD(b, a % b)

gcd = dif_spots[0]
for i in range(1, len(dif_spots)):
    gcd = GCD(gcd, dif_spots[i])

print(gcd)