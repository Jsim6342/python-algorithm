from itertools import combinations

while True:
    nums = list(map(int,input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    for lst in list(combinations(nums[1:], 6)):
        print(*lst)
    print()