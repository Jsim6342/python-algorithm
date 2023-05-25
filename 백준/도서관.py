N, M = map(int, input().split())
positions = list(map(int, input().split()))

minus_positions = [i for i in positions if i < 0]
plus_positions = [i for i in positions if i > 0]

minus_positions.sort()
plus_positions.sort(reverse=True)

result = 0

while minus_positions:
    move = abs(minus_positions[0])
    if len(minus_positions) > M:
        result += move * 2
        minus_positions = minus_positions[M:]
    else:
        result += move * 2
        break
    # print(result)
    
while plus_positions:
    move = plus_positions[0]
    if len(plus_positions) > M:
        result += move * 2
        plus_positions = plus_positions[M:]
    else:
        result += move * 2
        break
    # print(result)

print(result - max(list(abs(i) for i in positions)))


