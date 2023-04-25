def DFS(L):
    if L==m:
        global cnt # cnt 전역변수 참조
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt = cnt +1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1) # L+1 호출
             
            
if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*n #res에 여러 중복순열을 저장할 것임
    cnt=0 #마지막 갯수 출력
    DFS(0)
    print(cnt)