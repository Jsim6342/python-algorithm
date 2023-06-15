# 다음 array를 정렬
array = (('b', 1, '나'), ('c', 2, '라'), ('a', 3, '다'), ('a', 7, '가'), ('c', 3, '가'))

# 1. 가장 앞 요소로 내림차순 정렬
res1 = sorted(array, reverse=True)
print("res1 = ", res1)

# 2. 두 번째 요소로 내림차순 정렬
res2 = sorted(array, key = lambda x: x[1], reverse=True)
print("res2 = ", res2)

# 3. 첫 번째, 두 번째 요소로 오름차순 정렬
res3 = sorted(array, key = lambda x: (x[0], x[1]), reverse=True)
print("res3 = ", res3)

