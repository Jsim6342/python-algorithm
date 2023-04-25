# 주사위의 합을 새로운 리스트 cnt를 만들어 0으로 초기화 시키고 1씩 카운트 더해주는 방식

n, m = map(int, input().split())

cnt =[0]*(n+m+3)
max = -2147000000

#주사위 합 모두 더해서 cnt lst에 카운트 저장
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1
# 확률이 가장 많이 카운트 된 max값 구하기
for i in range(1, n+m+1):
    if cnt[i]>max:
        max=cnt[i]
# max 값과 일치하는 합 구하기
for i in range(1, n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
