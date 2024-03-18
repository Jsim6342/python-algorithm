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