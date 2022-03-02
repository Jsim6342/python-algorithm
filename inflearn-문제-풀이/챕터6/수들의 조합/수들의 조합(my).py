def DFS(L, s):
    global cnt
    if L==k:
        sumNum = 0
        sumNum = sum(res)
        if sumNum%m==0:
            cnt = cnt + 1
    else:
        for i in range(s, n):
            res[L]=a[i]
            DFS(L+1, i+1)


if __name__=="__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt=0
    res = [0]*k
    DFS(0,0)
    print(cnt)