# 1,5,10,50,100,500엔이 각각 모두 배수, 약수 관계이므로 그리디 가능.

money = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1]

res = 0
for change in changes:
    if money == 0:
        break
    res += money // change
    money = money % change
    # print(money, res)
    
print(res)