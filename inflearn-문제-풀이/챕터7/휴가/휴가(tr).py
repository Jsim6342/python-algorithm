def DFS(L,sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+t[L]<=n+1:
            DFS(L+t[L], sum+p[L]) #상담을 할 때
        DFS(L+1, sum) #상담을 안할 때

if __name__=="__main__":
    n = int(input())
    t = list()
    p = list()
    for i in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)
    res=-2147000000
    t.insert(0,0) #index를 날짜로 맞추기 위해 맨 앞에 0을 넣어 인덱스와 날짜를 맞춤
    p.insert(0,0)
    DFS(1,0)
    print(res)