N = int(input())

result = 0

for i in range(N):
    dice_numbers = list(map(int, input().split()))
    dice_count = dict()

    # 나온 주사위 수를 딕셔너리에 저장
    for number in dice_numbers:
        if number in dice_count.keys():
            dice_count[number] += 1
        else:
            dice_count[number] = 1
    
    # 중복된 수에 따른 상금 계산
    price = 0
    for key, value in dice_count.items():
        if value == 3:
            price = 10000 + key * 1000
        elif value == 2:
            price = 1000 + key * 100
    
    # 모두 다른 눈이 나오는 경우 상금 계산
    if price == 0:
        price = max(dice_count.values()) * 100

    # 최대 상금 갱신
    if price > result:
        result = price

print(result)

