def DFS(L):
    global cnt
    if L==0:
        print(cnt)
        return
    else:
        for x in coin:
            if L-x>0:
                cnt=cnt+1
                DFS(L-x)
            else:
                return
if __name__=="__main__":
    n = int(input())
    coin = list(map(int,input().split()))
    money = int(input())

    cnt=0
    DFS(money)


#   
#     def DFS(L, sum):
#     global cnt
#     global minNum
#     if sum==money:
#         if cnt<minNum:
#             minNum = cnt
#             print(minNum)
#             return
#     else:
#         for x in coin:
#             if sum<money:
#                 cnt=cnt+1
#                 DFS(L+1,sum+x)
#             else:
#                 return
# if __name__=="__main__":
#     n = int(input())
#     coin = list(map(int,input().split()))
#     money = int(input())

#     cnt=0
#     minNum=2174000000
#     DFS(0, money)