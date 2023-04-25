n = int(input())
a = list(map(int, input().split()))

# def reverse(x):
#     b=[]
#     reNum=""
#     for i in str(x):
#         b.append(i)
#     b.reverse()
#     for i in range(len(b)+1):
#         reNum+=b[i]
#         reNum=int(reNum)
#     return reNum

# def isprime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return False
#         else:
#             return True

# for i in a:
#     reNum = reverse(i)
#     if isprime(reNum):
#         print(reNum)


b=[]
    
for i in str(a):
    b.append(i)
b.reverse()
print(b)