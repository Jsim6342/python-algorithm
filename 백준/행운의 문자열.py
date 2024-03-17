# 시간 복잡도 = 3600만 * 10 = 3.6억
from itertools import permutations

def fact(x):
	if x == 0:
		return 1
	return fact(x-1) * x

count = 0
str = input()

for s in permutations(str, len(str)):
    flag = True
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            flag = False
            break
    if flag:
        count += 1
		
for x in range(ord('a'),ord('z')+1):
	count //= fact(str.count(chr(x)))

print(count)

# from itertools import permutations

# def fact(x):
# 	if x == 0:
# 		return 1
# 	return fact(x - 1) * x

# S = input()
# ans = 0

# for perm in permutations(S):
# 	ok = True
# 	for i in range(0, len(S) - 1):
# 		if perm[i] == perm[i + 1]:
# 			ok = False
# 			break
# 	ans += ok

# for i in range(ord('a'), ord('z') + 1):
# 	ans //= fact(S.count(chr(i)))

# print(ans)

    


    



