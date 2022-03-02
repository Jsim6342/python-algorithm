l = int(input())
high=list(map(int,input().split()))
m = int(input())

high.sort(reverse=True)
while m>0:
    high[0] -=1
    high[l-1] +=1
    high.sort(reverse=True)
    m -=1

print(high[0]-high[l-1])

# 맞음.
# 강사님은 sort를 내림차순으로 해서 풀었을 뿐 방법 도일