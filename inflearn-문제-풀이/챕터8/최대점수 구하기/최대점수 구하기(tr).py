# 한 문제당 1번만 풀어야 하므로, 중복을 방지하기 위해서 2차원 list로 풀어야한다.
# 바로 전 list index에 1번만 풀이한 문제의 list를 저장하고, 이를 참고하여 다음 index list에 냅색알고리즘을 전개한다.
# 하지만, 2차원 list로  할 경우 많은 메모리를 사용하기 때문에 지양하는 것이 좋다.
# 그래서 여기서는 1차원 list로 풀이함.
# 1차원 list로 푸는 방법은 0번 index 부터 탐색하는 것이 아닌, 끝번 index 부터 탐색하면 중복이 되지 않는다.
# dy[j]: j 시간이 주어졌을 때 얻을 수 있는 최대 점수
n, m = map(int,input().split())
dy=[0]*(m+1)
for i in range(n):
    s, t = map(int, input().split())
    for j in range(m,t-1,-1):
        dy[j]=max(dy[j],dy[j-t]+s)
print(dy[m]) 