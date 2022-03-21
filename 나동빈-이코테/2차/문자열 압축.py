def solution(s):
    answer = len(s)
    
    # 문자열을 자를 단위 설정 1 ~ len(s) // 2 + 1
    for cut_unit in range(1, len(s) // 2 + 1):
        now_str = ""
        prev_word = s[:cut_unit]
        count = 1
        
        # 각 단위 마다 문자열을 비교하고 now_str에 압축
        for i in range(cut_unit, len(s), cut_unit):
            if prev_word == s[i:i+cut_unit]: # 다음 문자열과 일치하면, 카운트 + 1
                count += 1
                continue
            else: # 일치하지 않으면, 해당 문자열을 카운트와 함께 저장
                if count != 1: now_str += str(count) + prev_word
                else: now_str += prev_word
                      
                prev_word = s[i:i+cut_unit]
                count = 1
        
        # 마지막 남아있는 문자열 처리
        if count != 1:
            now_str += str(count) + prev_word
        if now_str[len(now_str) - cut_unit:] != prev_word:
            now_str += prev_word
            
        # answer을 최솟값으로 갱신
        answer = min(answer, len(now_str))

    return answer

if __name__ == "__main__":
    s = "aabbaccc"
    print(solution(s))