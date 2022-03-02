'''전역변수와 지역변수'''
# 전역변수가 로컬에서 로컬변수로 언어번역 될 때 오류가 난다. (로컬엔 생성된 값이 아니므로)
# 보통 cnt = cnt + 1 과 같은 상황에서 발생(변수 안에 또 변수)

def DFS1(): #1. 지역변수 cnt를 확인 -> 2. 전역변수 cnt를 확인 (로컬변수를 우선)
    cnt=3 #지역변수 생성.
    print(cnt) 

def DFS2():
    global cnt #현재 함수 내 cnt가 전역변수임을 알림. 즉, 이후에 생성되는 cnt는 전역변수로 인식
    if cnt==5:
        cnt=cnt+1 #지역변수 생성. but 할당 자체가 되지 않음.
        print(cnt)

if __name__=="__main__":
    cnt=5 
    # 전역변수: main script에 선언된 변수. 
    # cnt=5 하는 순간 변수 생성과 5 할당. (생성, 할당)
    # 전역변수는 모든 함수가 접근, 값 변경 가능(공용이다.)
    DFS1()
    DFS2()
    print(cnt)

    # 그렇다면 list는 왜 명시해주지 않아도 전역변수로 잘 작동하는가??

def DFS():
    a[0]=7 #a[0]을 새로 생성하는 것이 아니라 변경한다. (참조하는 것)
    a=a+[4] #이런 경우 오류. a가 할당되지 않았기 때문에(전역변수 참조가 필요)
    global a # 전역 list로 알림.
    a=[7,8] #이런 경우 로컬 list인 지역 list가 생성된 것.
    
    print(a)

if __name__=="__main__":
    a=[1.2.3]
    DFS()
    print(a)
    