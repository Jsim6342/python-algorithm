def check(mid):
    check_num = houses[mid]
    result = 0
    for i in range(n):
        result += abs(check_num - houses[i])
    return result

n = int(input())
houses = list(map(int, input().split()))
houses.sort()

mid1 = len(houses) // 2 - 1
mid2 = len(houses) // 2
if check(mid1) >= check(mid2):
    print(houses[mid1])
else:
    print(houses[mid2])

