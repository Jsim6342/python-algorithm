N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

start = 0
end = max(trees)
result = 0

while start <= end:
    now_height = (start + end) // 2

    total_height = 0
    for tree in trees:
        temp = tree - now_height
        if temp >= 0:
            total_height += temp
    
    if total_height >= M:
        start = now_height + 1
        result = now_height
    else:
        end = now_height - 1

print(result)