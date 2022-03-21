n = input()

length = len(n) // 2

if sum(map(int, n[:length])) == sum(map(int,n[length:])):
    print("LUCKY")
else:
    print("READY")
