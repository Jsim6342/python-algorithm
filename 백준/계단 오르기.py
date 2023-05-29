# 각 지점마다 최댓값을 저장해 나가는 방식으로 바텀업

N = int(input())
score_list = [0]

for _ in range(N):
    score_list.append(int(input()))

f = [0] * (N + 1)
count = 0

def solve(f, index, count):
    if index >= N - 1:
        return
    if count == 3:
        count -= 1
        return
    
    f[index + 1] = max(f[index + 1] , f[index] + score_list[index + 1])
    solve(f, index + 1, count)
    
    f[index + 2] = max(f[index + 2], f[index] + score_list[index + 2])
    solve(f, index + 2, count + 1)


solve(f, 0, 0)

print(f)