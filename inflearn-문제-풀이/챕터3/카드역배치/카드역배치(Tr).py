a=list(range(21)) #0~20으로 찬 list 생성

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i]

a.pop(0) #0번 index 값 빼기(0을 빼기 위함)
for x in a:
    print(x, end=' ')