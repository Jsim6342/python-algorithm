import sys
input = sys.stdin.readline

a, b = map(int, input().split())

result = 0

# 풀이1
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)


# print('1' * gcd(a, b))

# 풀이2
while True:
	tmp = a % b
	a = b
	b = tmp
	if b == 0:
		result = a
		break
		
print('1' * result) # 결과인 GCD