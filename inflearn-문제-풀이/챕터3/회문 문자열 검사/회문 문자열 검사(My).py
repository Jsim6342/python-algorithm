n = int(input())

reverse=[]
result=[]
for i in range(n):
    a=input()
    a=a.upper()
    a=list(a)
    if a == list(reversed(a)):
        result.append("YES")
    else:
        result.append("NO")

for i in range(len(result)):
    print('#',i+1, sep='',end=' ')
    print(result[i])


#================================






   
 
