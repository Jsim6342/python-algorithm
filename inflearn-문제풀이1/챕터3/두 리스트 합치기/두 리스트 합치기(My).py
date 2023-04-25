n = int(input())
a=list(map(int,input().split()))
m = int(input())
b=list(map(int,input().split()))

res = a+b
res.sort()
print(res)

# 내 방법도 맞았지만, 포인터 변수를 이용한 방법이 시간복잡도 측면에서 효율적
# sort()는 n log n 횟수로 정렬시키는 방법.
# 리스트 크기가 n, m인 리스트의 합 정렬은 n+m회의 반복만에 정렬시킬 수 있다!