 # dy[j]: 가방에 담을 수 있는 무게가 j일 때, 보석의 최대 가치
n, m = map(int,input().split())
dy=[0]*(m+1)
for i in range(n): #보석의 갯수만큼 돌면서, dy list를 탐색
    w, v = map(int, input().split())
    for j in range(w,m+1):
        dy[j]=max(dy[j],dy[j-w]+v) #w가 담기기전의 가치에 현재 w의 가치 v를 더하여 기존의 값과 비교하여 최대값을 dy[j]에 기록
print(dy[m])