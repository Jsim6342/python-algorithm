def DFS(L):
    global cnt
    if L==m:
        for x in res:
            print(x, end=' ')
            cnt = cnt + 1
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
            ch[i]=0
            
if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*m
    ch = [0]*(n+1)
    cnt=0
    DFS(0)