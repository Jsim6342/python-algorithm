# reversed는 뒤집힌 리스트를 반환
a = input()
a = list(a)
print(a)
print(list(reversed(a)))

# reverse는 아무런 값도 반환하지 않지만, 리스트에 있는 값의 순서를 뒤집음
b = [1,2,3]
print(b)
b.reverse()
print(b)

#
a=[1,2,3,4]
for i in range(3,0,-1):
    print(a[i])


b = [0]*5
print(b)