def DFS(L, s):
    global cnt
    if L==m:
        for x in res:
            print(x, end=' ')
        cnt = cnt + 1
        print()
    else:
        for i in range(s,n+1):
                res[L]=i
                DFS(L+1, i+1)

            
if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt=0
    DFS(0,1)
    print(cnt)