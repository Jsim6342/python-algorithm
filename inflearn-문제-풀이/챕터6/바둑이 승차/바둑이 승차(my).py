def DFS(x, sum):
    global maxNum
    if x>=n:
        if c-sum>maxNum:
            maxNum = sum
    else:
        DFS(x+1, sum+a[x])
        DFS(x+1, sum)

if __name__=="__main__":

    c, n = map(int, input().split())
    a =[]
    for i in range(n):
        a.append(int(input()))
    maxNum = 0
    DFS(0, 0)
    print(maxNum)