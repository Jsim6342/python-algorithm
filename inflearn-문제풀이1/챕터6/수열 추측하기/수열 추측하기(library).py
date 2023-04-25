import itertools as it # 순열, 조합을 자동으로 구해줌
n, f = map(int, input().split())
n = [1]*n
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1)) # 1~n까지 리스트화
for tmp in it.permutations(a): #a list 값으로 만들 수 있는 순열을 tmp에 저장
    sum=0
    for L,x in enumerate(tmp):
        sum+=(x*b[L]) #b와 곱해주기 위해서 for에서 인덱스 값(L)을 함께 추출함.
    if sum==f: #합이 f와 같을 때
        for x in tmp:
            print(x, end=' ')
        break