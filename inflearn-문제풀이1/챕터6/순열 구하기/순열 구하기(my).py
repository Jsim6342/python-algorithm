def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end='')
            cnt=cnt+1
        return
    else:
        for i in range(len(a)):
            res[L]=a[i]
            a.pop(i) # pop을 하면서 list가 줄어들어 out of range 오류 발생
            DFS(L+1)

if __name__=="__main__":
    n, m = map(int, input().split())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    res = [0]*m
    cnt=0
    DFS(0)
    print(cnt)