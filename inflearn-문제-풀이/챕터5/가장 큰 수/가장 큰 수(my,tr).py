n, m = map(int, input().split())
num = list(map(int, str(n))) #n을 list화
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x: #stack이 비어있지 않고, m>0이고, stack 맨 뒷 자리가 x 보다 작다면
        stack.pop()
        m -= 1
    stack.append(x)
if m!=0: #아직 m을 모두 소모시키지 않았을 경우,
    stack=stack[:-m] #맨 앞에서 부터 -m 인덱스 까지 자름. 뒤 쪽의 m개의 자료가 날아감
res=''.join(map(str,stack)) #string을 join. string 붙여주기.
print(res)