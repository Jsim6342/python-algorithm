k, n = map(int, input().split())
a_list=[]
for _ in range(k):
    a = int(input())
    a_list.append(a)

# 이분 검색을 위한 lt, rt 선언
lt=1
rt=max(a_list) #가장 긴 길이는 max값을 넘지 못할 것임

midRes=0
while lt<=rt:
    sum=0
    res=(lt+rt)//2
    for x in a_list:
        sum+=x//res
    if n==sum:
        midRes=res
        break
    elif n>sum: #sum이 길다.
        rt=res-1
    else:
        lt=res+1

while lt<=rt:
    res=(lt+rt)//2
    if midRes==res:
        print(res)
        break
    elif midRes>res:
        rt=res-1
    else:
        lt=res+1
#20점... 공부 더 필요..