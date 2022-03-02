card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

c=[]
cnt=0
for i in range(2):
    a,b = map(int,input().split())
    for j in range(a-1,b):
        cnt+=1
        card[j]=card[b-cnt]
print(card)