from collections import deque
n = int(input())
a=[]
for _ in range(n):
    a.append(input())

b=[]
for _ in range(n-1):
	b.append(input())

a = deque(a)

while len(a)!=1:
    for i in range(len(b)):
        if b[i]==a[0]:
            a.popleft()

print(a[0])		
#틀림..