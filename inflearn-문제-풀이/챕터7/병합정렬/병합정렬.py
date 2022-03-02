# 병합정렬은 후위 순회이다.
# 먼저 DFS 재귀함수로 후위순회를 거쳐 탐색한 뒤, 나눠진 2개의 리스트를 병합해가며 순차적으로 정렬해가는 방식
# DFS 후위순회와 두 리스트 합치기 알고리즘이 합쳐짐.
def Dsort(lt, rt):
    if lt<rt:
        mid=(lt+rt)//2
        Dsort(lt,mid)
        Dsort(mid+1,rt)
        p1=lt
        p2=mid+1
        tmp=[]
        while p1<=mid and p2<=rt: # mid를 기준으로 하여 나눠진 2개의 list를 정렬한다. 
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: tmp=tmp+arr[p1:mid+1] #만약 p1이 남아 있다면, 남은 list 넣어주기
        if p2<=rt: tmp=tmp+arr[p2:rt+1] #만약 p2가 남아 있다면, 남은 list 넣어주기
        for i in range(len(tmp)): #만들어진 tmp list를 원래의 arr list에 넣어줘야 한다.
            arr[lt+i]=tmp[i]

if __name__=="__main__":
    arr=[23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort: ", end='')
    print(arr)
    Dsort(0,7)
    print()
    print("After sort: ", end='')
    print(arr)