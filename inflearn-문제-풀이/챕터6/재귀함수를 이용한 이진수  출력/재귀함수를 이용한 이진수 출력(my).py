def change(num):
    if num>0:
        res+=str(num%2)
        change(num)
        
n = int(input())
change(n)
print(res)

#메모리가 스택으로 쌓이고 제거되는 형식으로 재귀함수는 실행되기 때문에 지역변수 res가 출력될 수 없는듯..