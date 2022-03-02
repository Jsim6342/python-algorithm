import random
n, k = map(int, input().split())

a=list(map(int,input().split()))

#list에서 3장 뽑는 기능 어떻게 하지...?

#====================================
n, k = map(int, input().split())
a=list(map(int,input().split()))
res=set() #set은 중복을 제거한다.
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m]) #set은 add로 값을 넣는다.
res=list(res) # set은 sort함수가 없어 list로 변환.
res.sort(reverse=True) #resverse=True는 내림차순
print(res[k-1])