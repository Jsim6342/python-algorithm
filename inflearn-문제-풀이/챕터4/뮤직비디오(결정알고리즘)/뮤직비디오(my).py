# 주어진 길이에 맞게 만들 수 있는 경우의 수
n, m = map(int, input().split())
a = list(map(int, input().split()))

#문제: n개로 만들 수 있는 똑같은 최소 길이의 m개의 영상의 길이 출력
#조건: 가장 최소 길이, 연속적으로만 더할 수 있다.
#문제 잘못이해함!!!! -> 최소 용량 DVD m개로 모든 영상을 녹화할 수 있는 m을 구하는 것!
#가장 최소 길이: lt, 가장 최대 길이 rt

# 근데 결정 알고리즘으로 안품...
# 내 풀이는 list를 돌면서 연속적으로 더할 수 있는 합을 인덱스로 하여 check list에 +1 시키고
# 그 횟수가 m번이 된 check index 값만 따로 뽑아내어 최소값을 구함.
res = []
check = [0]*sum(a)


for i in range(n):
    for j in range(i+1,n):
        tmp = sum(a[i:j])
        check[tmp] +=1
for i in range(len(check)):
    if check[i]==m:
        res.append(i)
print(min(res))

# 근데 틀렸고,,,
# 아 문제를 잘못이해한듯...