def solution(s):
    answer = 1

    # 홀수 팰린드롬 카운트
    for i in range(len(s)):
        count = 1
        while True:
            if i - count < 0 or i + count >= len(s):
                answer = max(answer, (count-1) * 2 + 1)
                break
                
            if s[i-count] == s[i+count]:
                count += 1
            else:
                answer = max(answer, (count-1) * 2 + 1)
                break

    # 짝수 팰린드롬 카운트
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            continue
        
        count = 1
        while True:
            if i - count < 0 or i + 1 + count  >= len(s):
                answer = max(answer, (count-1) * 2 + 2)
                break
                
            if s[i-count] == s[i+1+count]:
                count += 1
            else:
                answer = max(answer, (count-1) * 2 + 2)
                break
                
    return answer 

if __name__ == "__main__":
    s = "abcdcba"
    print(solution(s))