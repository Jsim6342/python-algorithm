import math

n = int(input())

a= list(map(int,input().split()))

sum=0
avg=0
for i in range(0,len(a)):
    sum=sum+a[i]
    if i==len(a)-1:
        avg = sum/len(a)
        avg = math.ceil(avg)

x=float('inf')
result=0
resultNum=0
for i in range(0,len(a)):
    if abs(avg-a[i])<=x and a[i]>result:
        x = abs(avg-a[i])
        result = a[i]
        resultNum = i+1

print(avg, resultNum)


#================================
# n = map(int, input())
# a= list(map(int,input().split()))

# ave=round(sum(a)/n) #round: 소수 첫 째 자리 반올림, sum: 합 함수

# min=2147000000 #정수형 가장 큰 수
# for idx, x in enumerate(a): #enumerate: idx에는 index 대응, x에는 값이 대응
#     tmp=abs(x-ave)
#     if tmp<min:
#         min=tmp
#         score=x
#         res=idx+1
#     elif tmp==min:
#         if x>score:
#             socre=x
#             res=idx+1