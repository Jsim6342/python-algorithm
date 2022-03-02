#주어진 리스트 순서대로 증가수열을 만들 수 있는 경우의 수 중 가장 긴 길이를 출력

n = int(input())
a = list(map(int, input().split()))
a.insert(0,0) # 입력받은 list를 1번 index 부터 시작하게 하기 위해서
dy = [0] * (n+1) #a list의 index 번호까지 가장 긴 수열의 길이를 저장하는 list
dy[1] = 1
res=0
for i in range(2,n+1):
    max=0
    for j in range(i-1, 0, -1): #현재 index 보다 전 index 수들을 탐색
        if a[j]<a[i] and dy[j]>max: #현재 index 보다 값이 작으면서, 그 중 가장 큰 값의 증가수열 길이를 max에 저장
            max=dy[j]
    dy[i]= max+1 # 구해진 max값에 +1을 하여 현재 증가수열 최대 길이 dy list의 해당 index에 기록
    if dy[i]>res:# dy list의 최대값이 답이 된다.
        res=dy[i]
print(res)
