n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))

#meeting.sort()를 하면 앞의 자료를 기준으로 정렬된다.. 이를 방지하기 위해 조건설정이 필요.
meeting.sort(key=lambda x : (x[1], x[0])) # 뒤를 기준으로 정렬하는 정렬법
et=0 #현재 회의가 끝나는 시간
cnt=0 
for s, e in meeting:
    if s>=et: #과거 회의가 끝난시간 보다 시작시간이 같거나 크면,
        et=e #끝나는 시간을 현 회의 시간으로 하고
        cnt+=1
print(cnt)