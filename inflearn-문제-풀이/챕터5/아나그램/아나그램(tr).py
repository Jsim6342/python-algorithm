a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys(): #key값이 없고,
        if str1[i]!=str2[i]: #key값에 할당된 value값이 같지 않다면,
            print("NO")
            break
    else:
        print("NO")
else:
    print("YES")