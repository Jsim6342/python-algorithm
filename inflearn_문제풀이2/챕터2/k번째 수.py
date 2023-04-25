T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    focus_numbers = numbers[s-1:e]

    focus_numbers.sort()
    print("#%d %d" % (i + 1, focus_numbers[k - 1]))
