# 키로 정렬 후, 나 보다 키 큰 사람들과 몸무게 비교시 높으면 카운팅

n = int(input())
info = []
for i in range(n):
    k, m = map(int,input().split())
    info.append([k,m])

info.sort(reverse=True)

largest = 0
cnt = 0
for i in range(n):
    if largest < info[i][1]:
        largest = info[i][1]
        cnt+=1
print(cnt)

# 맞음!