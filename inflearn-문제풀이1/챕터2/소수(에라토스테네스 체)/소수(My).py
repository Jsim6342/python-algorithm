# 답은 맞는거 같은데 time limit이래...
n = int(input())

result=0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        result+=1

print(result)  