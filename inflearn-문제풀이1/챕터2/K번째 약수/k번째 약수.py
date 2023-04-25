#import sys
#sys.stdin=open("input", "rt")

n, k = map(int, input().split()) #띄어쓰기를 기준으로 숫자를 받아내어 int형 변환

cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else: #for이 break가 아니라 정상적으로 끝나면 수행
    print(-1)