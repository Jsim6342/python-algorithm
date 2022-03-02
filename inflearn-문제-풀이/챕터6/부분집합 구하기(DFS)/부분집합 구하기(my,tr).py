def DFS(v):
    if v==n+1: #깊이탐색 종료지점(체크된 0,1에 따라 출력)
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
    else:
        ch[v]=1 #해당 원소를 포함한다 = 1
        DFS(v+1)
        ch[v]=0 #해당 원솔즐 포함하지 않는다 = 0
        DFS(v+1)


if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1) #원소를 사용했는지 안했는지 구분하기 위해 선언
    DFS(1)