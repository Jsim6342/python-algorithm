n = int(input())
a= list(map(int,input().split()))

#round: 소수 첫 째 자리 반올림, sum: 합 함수
#round는 round_half_even 방식을 택한다.(절반 값에선 짝수 쪽으로 반올림 해버린다.)
# 따라서 쓰면 안됨!
# ave=round(sum(a)/n) 
# 아래와 같은 방법을 사용하자
ave=sum(a)/n+0.5 # 0.5를 더하고
ave=int(ave) # int로 소수점 버리기


min=2147000000 #정수형 가장 큰 수
 =for idx, x in enumerate(a): #enumerate: idx에는 index 대응, x에는 값이 대응
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            socre=x
            res=idx+1
 print(ave, res)