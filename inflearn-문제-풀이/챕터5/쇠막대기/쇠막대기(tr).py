# 스택을 사용해서 풀이
a = input()
stack= []
cnt=0

for i in range(len(a)):
    
    if a[i]=='(':
	    stack.append(a[i])
    else:
        if a[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else: #마지막 남은 부분 카운팅
            stack.pop()
            cnt+=1
print(cnt)
# 왜 오류나는지 모름....