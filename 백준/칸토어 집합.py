# 시간 복잡도 3^N
# 시간 복잡도 계산 = 3^12

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
