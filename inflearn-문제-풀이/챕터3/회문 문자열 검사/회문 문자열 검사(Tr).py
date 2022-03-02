#방법1
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d No" %(i+1))
            break
        else:
            print("#%d No" %(i+1))

#방법2
# n = int(input())
# for in in range(n):
#     s=input()
#     s=s.upper()
#     if s==s[::-1]: #s[::-1]이 list를 뒤집는 역할을 한다.
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))