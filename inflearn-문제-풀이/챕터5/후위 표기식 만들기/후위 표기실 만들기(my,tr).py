a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal(): #숫자이면,
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=="*" or stack[-1]=='/'): #*,/ 보다 높은 연산자를 꺼내야 함.
                res+=stack.pop() #끄집어 내고 저장
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and (stack[-1]!='('): # +,- 보다 높은 연산자를 뽑아야함.
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                 res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()

print(res)