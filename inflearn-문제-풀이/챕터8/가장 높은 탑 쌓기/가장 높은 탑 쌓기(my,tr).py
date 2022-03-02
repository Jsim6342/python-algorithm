# 최대 부분 증가수열과 동일한 맥락의 문제
n = int(input())
bricks = []
for i  in range(n):
    a, b, c = map(int,input().split())
    bricks.append((a,b,c))
bricks.sort(reverse=True) # sort는 튜플 자료의 첫 번째 자료가 기준이된다.(설정가능) 너비 기준으로 내림차순 정렬
dy=[0]*n
dy[0]=bricks[0][1] #[벽돌번호][0:벽돌의너비, 1:높이, 2:무게]
res=bricks[0][1]
for i in range(1,n):
    max_h=0;
    for j in range(i-1,-1, -1):
        if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
            max_h=dy[j]
    dy[i]=max_h+bricks[i][1]
    res = max(res, dy[i])
print(res)

