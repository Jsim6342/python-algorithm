n, c =map(int, input().split())

distinict= []
for i in range(n):
    distinict = int(input())

lt = min(distinict)
rt = max(distinict) - min(distinict)

while lt<=rt:
    mid = (lt+rt)//2


    # 그냥 영상 봄..