def DFS(L,sum):
    if L==k:
        sumList[sum] = 0
    else:
        DFS(L+1,sum+w[L]) #추를 오른쪽에 놓는 경우
        DFS(L+1,sum-w[L]) #추를 왼쪽에 놓는 경우
        DFS(L+1,sum) #추를 놓지 않는 경우
if __name__=="__main__":
    k = int(input())
    w = list(map(int,input().split()))
    s = sum(w)
    sumList = []
    for i in range(s+1):
        sumList.append(i)
    DFS(0,0)
    cnt=0
    for i in range(len(sumList)):
        if sumList[i]!=0:
            cnt += 1
    print(cnt)
    # 뭐가 문젠지 모르겠지만, 틀림