
def DFS(L):
    global res
    if L==n:
        cha = max(money)-min(money)
        if cha<res:
            tmp=set() # 두 명의 금액이 중복될 경우를 없애기 위해 set자료 이용
            for x in money:
                tmp.add(x)
            if len(tmp)==3: # tmp 길이가 3이면 중복이 없다고 할 수 있다.
                res=cha

    else:
        for i in range(3): #3명의 인원에게 각각 돈을 나눠줌
            money[i]+=coin[L] #돈을 준 상황
            DFS(L+1)
            money[i]-=coin[L] #돈을 빼준 상황

if __name__=="__main__":
    n = int(input())
    coin = []
    money = [0] * 3 # 각각 인덱스는 사람을 의미
    for _ in range(n):
        coin.append(int(input()))
    res = 2147000000
    DFS(0)  # list를 매개변수로 넣을 순 없나보다..
    print(res)
   