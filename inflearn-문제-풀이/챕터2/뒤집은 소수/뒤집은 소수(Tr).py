n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if  x==1:
        return False
    for i in range(2,x//2+1): #보통 소수가 아닌 수들은 절반 내에 약수가 존재
        if x%i==0:
            return False
    else: 
        return True


for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
