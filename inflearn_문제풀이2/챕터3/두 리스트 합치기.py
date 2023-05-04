N = int(input())
list_a = list(map(int, input().split()))
M = int(input())
list_b = list(map(int, input().split()))

result = list_a + list_b
result.sort()

for x in result:
    print(x, end=' ')
