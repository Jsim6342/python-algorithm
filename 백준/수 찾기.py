import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

numbers.sort()

def binary_search(arr, target):
    cur = -1
    step = len(arr)
    while step != 0:
        while (cur+step < len(arr) and arr[cur+step] <= target):
            cur += step
        step //= 2
    return arr[cur] == target

for number in check_list:
    if binary_search(numbers, number):
        print(1)
    else:
        print(0)