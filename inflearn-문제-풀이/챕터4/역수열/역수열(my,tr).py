# 0으로 구성된 리스트를 선언
# 내림차순으로 1~n 까지 정렬 후, 0으로 구성된 리스트에 1부터 차례차례 채워넣는다
# 채워넣는 원리는 내 앞에 큰 숫자가 몇 개인지에 따라 그 갯수만큼 오른쪽으로 index 이동 후 넣는다.

n = int(input())
a = list(map(int,input().split()))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0: #a[i]==0은 빈공간을 찾았다. seq[j]==0: 이미 0이 배정될 경우 다음 자리를 찾는다.
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x)