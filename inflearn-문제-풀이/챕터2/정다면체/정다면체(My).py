# dictinonary로 푸려다 멈춤..
n, m = map(int, input().split())

list=[]
for i in range(n+1):
    for j in range(m+1):
        list.append(i+j)

count={}
for i in list:
    try: count[i] += 1
    except: count[i] = 1

# for i,x in enumerate(count):
#     if count[i].values()==max(count.values()):
        

print(count)
print(max(count.keys()))