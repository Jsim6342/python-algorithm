# 자르는 횟수 2^N-1 회
# 시간복잡도 계산 2^12-1 = 약 4000번

def cut_str(str, now_num):
    if now_num == 1:
        return "-"
    
    div_num = now_num//3
    for i in range(div_num,div_num*2):
        str[i] = " "

    return cut_str(str[:div_num], div_num) + ''.join(str[div_num:div_num*2]) + cut_str(str[div_num*2:], div_num)
    
    
while True:
    try:
        N = int(input())
        now_num = 3 ** N
        str = ["-"]*now_num
        print(cut_str(str, now_num))
    except:
        break
