# 키로 정렬 후, 나 보다 키 큰 사람들과 몸무게 비교시 높으면 카운팅

n = int(input())
body = []
for i in range(n):
    k, m = map(int,input().split())
    body.append([k,m])

body.sort(reverse=True)

largest = 0
cnt = 0
for x,y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)