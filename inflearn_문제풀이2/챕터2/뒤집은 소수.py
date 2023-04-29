def isPrime(x):
    return

def reverse(x):
    return

N = int(input())
numbers = list(input().split())

for number in numbers:
    word_number = []
    for word in number:
        word_number.append(word)
    reverse_number = ""
    for word in word_number[::-1]:
        reverse_number += word
    print(int(reverse_number))