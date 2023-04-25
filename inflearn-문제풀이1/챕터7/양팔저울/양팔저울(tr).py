def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=s: #음수는 고려하지 않아도 된다.
            res.add(sum)
    else:
        DFS(L+1,sum+G[L]) #추를 오른쪽에 놓는 경우
        DFS(L+1,sum-G[L]) #추를 왼쪽에 놓는 경우
        DFS(L+1,sum) #추를 놓지 않는 경우
if __name__=="__main__":
    n = int(input())
    G = list(map(int,input().split()))
    s = sum(G)
    res = set() # 측정될 수 있는 물의 무게들을 res에 추가 (중복 방지를 위해 set 자료구조 사용)
    DFS(0,0)
    print(s-len(res))