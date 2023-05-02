N = int(input())


for i in range(N):
    word = input()
    result = "YES"
    
    for j in range(len(word)):
        if word[j].upper() != word[-(j+1)].upper():
            result = "NO"
            break
    
    print(str("#" + str(i + 1) + " " + result))