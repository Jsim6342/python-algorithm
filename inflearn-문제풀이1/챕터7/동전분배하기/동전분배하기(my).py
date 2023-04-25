
def DFS(L, a, b, c):
    global res
    if L==n:
        maxNum = max(sum(a),sum(b),sum(c))
        minNum = min(sum(a),sum(b),sum(c))
        div = maxNum - minNum
        if res>div:
            res=div
        return
    else:
        DFS(L+1, a.append(money[L]), b, c)
        DFS(L+1, a, b.append(money[L]), c)
        DFS(L+1, a, b, c.append(money[L]))

if __name__=="__main__":
    n = int(input())
    money = list()
    for i in range(n):
        money.append(int(input()))
    a = []
    b = []
    c = []
    res = 2147000000
    DFS(0, a, b, c)  # list를 매개변수로 넣을 순 없나보다..
    print(res)
   