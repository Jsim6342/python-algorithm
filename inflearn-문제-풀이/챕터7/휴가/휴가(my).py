def DFS(L,time,sum):
    global res
    if time>n:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, time+t[L], sum+p[L])
        DFS(L+1, time, sum)


if __name__=="__main__":
    n = int(input())
    t = list()
    p = list()
    for i in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)
    res=-2147000000
    DFS(0,0,0)
    print(res)