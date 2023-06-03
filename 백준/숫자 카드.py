import sys

N = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
give_cards = list(map(int, sys.stdin.readline().split()))

my_cards.sort()
result = []

def binary_search(arr, target):
    left, right = 0, N-1
    check = False
    while left <= right:
        mid = (left + right) // 2
        if my_cards[mid] > target:
            right = mid - 1
        elif my_cards[mid] < target:
            left = mid + 1
        else:
            check = True
            break
    return check


for num in give_cards:
    if binary_search(my_cards, num):
        result.append(1)
    else:
        result.append(0)

print(*result)