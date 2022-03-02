a = input()
b = input()

a_dic = dict()
for x in a:
    a_dic[x]=a_dic.get(x,0)+1

b_dic = dict()
for x in b:
    b_dic[x]=b_dic.get(x,0)+1

if a_dic == b_dic:
    print("YES")
else:
    print("NO")


# 딕셔너리 활용 능력이 부족. 알고리즘은 맞았음. 강의 조금 참고해서 품