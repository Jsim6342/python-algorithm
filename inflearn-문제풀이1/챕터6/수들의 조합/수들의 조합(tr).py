# 강사님 풀이법은 내 풀이법 if에서 sum을 검증하는 방법을 매개변수로 처리함.
def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])

if __name__=="__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)