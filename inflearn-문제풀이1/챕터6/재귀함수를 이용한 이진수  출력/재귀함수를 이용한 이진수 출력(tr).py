def DFS(x):
    if x==0:
        return #return만 적을 경우, 함수 종료
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    n = int(input())
    DFS(n)