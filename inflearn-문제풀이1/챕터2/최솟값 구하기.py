#최소값 구하기
#최종적으로 list에서 가장 작은 값이 저장되서 출력되게.

arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float('inf') #inf는 파이썬에서 가장 큰 값. 양의 무한대. 가장 큰 값을 넣어두자.
                    #float('inf') 대신에 arr[0]의 값을 넣어놔도 된다.
#방법1
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
print(arrMin)

#방법2
for x in arr:
    if x<arrMin:
        arrMin=x
print(arrMin)
