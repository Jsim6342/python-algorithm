# 주어진 리스트에서 10 값 인덱스 구하기
array = [1, 3, 3, 4, 5, 7, 9, 10, 11, 13, 13, 16]
target = 10

def binary_search(arr, target):
    lt = 0
    rt = len(arr) - 1

    while lt <= rt:
        mid = (lt + rt) // 2

        if arr[mid] < target:
            lt = mid + 1
        elif arr[mid] > target:
            rt = mid - 1
        else:
            return mid

print(binary_search(array, 10))
        
