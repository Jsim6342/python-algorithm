def DFS(v):
    global cnt
    if v==n:
        cnt = cnt + 1
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0 #체크 풀어주기
            
if __name__=="__main__":
    n, m = map(int, input().split())
    g = [[0]*(n+1) for _ in range(n+1)] # 그래프 선언
    
    #방향 그래프 체크
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
        
    ch = [0]*(n+1) #노드 번호 체크 리스트
    cnt = 0
    ch[1]=1 #1번 노드 방문 체크
    DFS(1)
    print(cnt)