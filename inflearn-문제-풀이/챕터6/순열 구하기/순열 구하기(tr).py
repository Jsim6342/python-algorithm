# check list를 만드는 것이 포인트!
def DFS(L):
    global cnt
    if L==m: #종착지점
        for j in range(L): #L, m 모두 가능
            print(res[j], end='')
        print()
        cnt=cnt+1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1) # DFS()함수를 기준으로 위는 호출내역, 아래는 스택에서 백하여 되돌아 왔을 때를 의미
                ch[i]=0
            
if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*n # n을 m크기로 해도 된다. 아마 여유롭게 해주려고 n으로 준 듯.
    ch = [0]*(n+1) # 0번 인덱스를 두어도 상관없다, (오히려 생각하기 편함.)
    cnt = 0
    DFS(0)
    print(cnt)