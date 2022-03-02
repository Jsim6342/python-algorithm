def DFS(L, sum):
    global res
    if L>res: #res 보다 큰 레벨값은 갈 필요가 없다.
        return
    if sum>money:
        return
    if sum==money:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])
            
if __name__=="__main__":
    n = int(input())
    coin = list(map(int,input().split()))
    money = int(input())
    res=2147000000
    coin.sort(reverse=True) # 1원 부터 시작하면 깊이 탐색에서 너무 많은 경우의 수 발생. 따라서 내림차순
    DFS(0, 0)
    print(res)