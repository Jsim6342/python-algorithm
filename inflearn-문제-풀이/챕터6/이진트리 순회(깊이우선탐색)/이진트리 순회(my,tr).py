def DFS(v): #깊이우선탐색 기본 구조는 if else
    if v>7:
        return
    else:
        print(v, end=' ') #전위순회. #DFS의 작업 함수 부분. 여기서는 출력. 보통 전위순회 문제 많음.
        DFS(v*2) #왼쪽
        #print(v, end=' ') #중위순회
        DFS(v*2+1) #오른쪽
        #print(v, end=' ') #후위순회. 대표적으로 병합정렬에서 이용

if __name__=="__main__":
    DFS(1)