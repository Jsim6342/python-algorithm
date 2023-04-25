# 부분집합 문제라고 생각
# 재도전 필요!
def DFS(L, sum):
    global result
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L]) #부분집합에 참여
        DFS(L+1, sum) #부분집합에 미참여

if __name__=="__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    DFS(0,0)