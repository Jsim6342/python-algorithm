# 리스트 크기가 n, m인 리스트의 합 정렬은 n+m회의 반복만에 정렬시킬 수 있다!
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

p1=p2=0 # 각 list 값을 가리키는 pointer를 선언
c=[] # 새롭게 담을 list 선언

# p1,p2를 각각 비교하면서 c list에 옮겨담음
while p1<n and p2<m: 
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

# p1, p2 남아있는 요소들을 list에 붙임
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

for x in c:
    print(x, end=' ')