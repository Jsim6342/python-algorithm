def DFS(L, sum):
    global cnt
    if sum>t:
        return # time lmite 피하기 위함
    if L==k:
        if sum==t:
            cnt=cnt+1

    else:
        for i in range(n[L]+1):
            DFS(L+1,sum+p[L]*i)


if __name__=="__main__":
    t = int(input())
    k = int(input())
    p = list()
    n = list()
    for i in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)
    cnt=0
    DFS(0,0)
    print(cnt)