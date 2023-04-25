# 시간복잡도를 줄이기 위해서는 sum>total//2 이면, 그 이후의 계산은 무의미하다.
import sys

def DFS(L, sum): #sum에 내가 만든 부분집합의 합을 계속 누적. L은 a의 index번호
    if sum>total//2:
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0) #프로그램을 종료
        else:
            print("NO")
    else:
        DFS(L+1, sum+a[L]) #현재 원소를 더하고 간다
        DFS(L+1, sum) #현재 원소를 건너뛰고, 그대로 진행한다

    
if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total=sum(a)
    DFS(0,0)
    print("NO")
    