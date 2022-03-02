# 풀이법: 검사하려는 5개 수에서 가운데 수를 기준으로 양옆 수는 같아야한다는 원리
a = [list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(7):
    for j in range(2,5):
        # 행 회문열 검사
        if a[i][j-1]==a[i][j+1] and a[i][j-2]==a[i][j+2]:
            cnt+=1
        # 열 회문열 검사
        if a[j-1][i]==a[j+1][i] and a[j-2][i]==a[j+2][i]:
            cnt+=1
print(cnt)

#정답!!