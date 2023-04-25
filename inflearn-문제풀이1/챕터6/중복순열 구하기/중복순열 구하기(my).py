def DFS(L):
    if L<=n:
        print(res)
    else:
        res[L]=L
        for i in range(L+1,n):
            DFS(i)
    

if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*n #res에 여러 중복순열을 저장할 것임
    cnt=0 #마지막 갯수 출력
    DFS(0)