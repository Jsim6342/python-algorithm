#풀이법: i가 0일 때 부터 시작해서 5개씩 묶어서 차례로 검사

board = [list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]: #tmp[::-1] 회문 시키는 방법
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
             cnt+=1
print(cnt)