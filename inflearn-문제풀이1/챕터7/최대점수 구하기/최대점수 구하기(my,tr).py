def DFS(L, sum, time):
    global res
    if time>m: #시간제한 적용 
        return
    if n==L:
        if sum>res:
            res=sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L]) #문제를 푸는 경우
        DFS(L+1, sum, time) #문제를 안푸는 경우


if __name__=="__main__":
    n, m = map(int,input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0,0,0)
    print(res)