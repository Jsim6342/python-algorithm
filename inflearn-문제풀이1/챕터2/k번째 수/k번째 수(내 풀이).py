T = int(input())
for t in range(1,T+1):
    N, s, e, k = map(int, input().split())

    list=[]
    for i in range(1,N+1):
        list.append(int(input()))

    list_2=[]
    for j in range(s,e):
        list_2.append(list[j])

    list_2.sort()

    result = list_2[k+1]
    print('#'+t, result, end=' ')

# =====================================

T=int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    # print(a[k-1])
    print("#%d %d" %(t+1, a(k-1)))