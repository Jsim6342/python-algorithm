N, M = map(int, input().split())
rice_cakes = list(map(int, input().split()))

rice_cakes.sort()

lt = 0
rt = max(rice_cakes)

result = 0
while lt <= rt:
    mid = (lt + rt) // 2

    total = 0
    for rice_cake in rice_cakes:
        temp = rice_cake - mid
        if temp > 0:
            total += temp
    
    if total >= M:
        lt = mid + 1
        result = mid
    else:
        rt = mid - 1

print(result)