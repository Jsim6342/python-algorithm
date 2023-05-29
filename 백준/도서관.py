# 풀이법
# 음수, 양수 나누어 왔다갔다를 해야하기 때문에 움직임 2번씩 카운트(이 때 한 번에 옮길 수 있는 도서만큼 제외)
# 가장 먼 거리를 1번만 가는게 최소이므로 가장 먼 거리를 마지막에 빼준다
 
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


