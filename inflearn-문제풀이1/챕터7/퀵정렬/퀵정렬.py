# 퀵정렬은 전위 순회이다.
# pivot은 기준이 되는 숫자로 보통 list의 맨 앞, 가운데, 맨 뒤 숫자를 기준으로 한다. (기준에 따라 성능이 달라짐)
# pos는 앞에서부터 순차적으로 가리키는 숫자이다.
# arr[i]와 pivot값과 비교. arr[i]<pivot일 때, pos가 가리키는 값과 arr[i]를 스왑한다.
# 맨 마지막에 pos와 pivot값을 스왑해주면, list는 pivot값 보다 작은 수들은 앞에, 큰 수들은 뒤에 위치하게 된다.
def Qsort(lt, rt):
    if lt<rt:
        pos=lt
        pivot=arr[rt]
        for i in range(lt, rt):
            if arr[i]<=pivot:
                arr[i], arr[pos] = arr[pos], arr[i] #변수 바꾸기. python 기본 문법
                pos+=1
        arr[rt], arr[pos] = arr[pos], arr[rt] #마지막에 pos와 pivot값 스왑
        #DFS 탐색 시작
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)


if __name__=="__main__":
    arr=[45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Before sort: ", end='')
    print(arr)
    Qsort(0,9)
    print()
    print("After sort: ", end='')
    print(arr)