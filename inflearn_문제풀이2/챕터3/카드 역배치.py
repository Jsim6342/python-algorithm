cards = []
for i in range(21):
    cards.append(i)


for _ in range(10):
    # input 받기
    start, end = map(int, input().split())

    # reverse할 리스트 추출
    # 해당 리스트를 reverse 한 후, 해당 index 지점을 바꿔준다.
    reverse_cards = cards[start:end + 1][::-1]

    index = 0
    for i in range(start, end + 1):
        cards[i] = reverse_cards[index]
        index += 1

for card in cards[1::]:
    print(card, end = ' ')

    


