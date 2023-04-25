def DFS(len):
    if dy[len]>0: #DFS lne 값이 구해져있으면 바로 return 시켜라 (메모이제이션)
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n= int(input())
    dy=[0]*(n+1)
    print(DFS(n))