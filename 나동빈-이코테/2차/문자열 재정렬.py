
s = input()

alphabets = []
numbers = []

for word in s:
    if word.isalpha():
        alphabets.append(word)
    else:
        numbers.append(int(word))

alphabets.sort()
print("".join(alphabets) + str(sum(numbers)))