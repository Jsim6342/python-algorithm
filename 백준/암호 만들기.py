# 주어진 문자열 사전순 정렬 후, 조합 뽑기

L, C = map(int, input().split())
words = list(input().split())
words.sort()

choose = []
answer = []

vowels = ('a', 'e', 'i', 'o', 'u')

def combination(index, level):
    if level == L:
        answer.append("".join(choose))
        return
    
    for i in range(index, C):
        choose.append(words[i])
        combination(i+1, level+1)
        choose.pop()

combination(0, 0)

for words in answer:
    count = 0
    for word in words:
        if word in vowels:
            count += 1
    if count >= 1 and count <= L - 2:
        print("".join(words))