import sys
import math
T = int(sys.stdin.readline())

def check_palindrome(word):
    end = math.ceil(len(word) / 2)
    lt = 0
    rt = len(word) - 1
    check = True

    for _ in range(end):
        if word[lt] == word[rt]:
            lt += 1
            rt -= 1
            continue
        else:
            check = False
            return [check, lt, rt]
    return [check, lt, rt]

for _ in range(T):
    word = str(sys.stdin.readline().rstrip())

    result, lt, rt = check_palindrome(word)

    if result:
        print(0)
    else:
        word_list1 = list(word)
        word_list2 = list(word)
        word_list1.pop(lt)
        word_list2.pop(rt)
        word1 = ''.join(word_list1)
        word2 = ''.join(word_list2)

        if check_palindrome(word1)[0] or check_palindrome(word2)[0]:
            print(1)
        else:
            print(2)

