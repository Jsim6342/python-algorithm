columns = set()
diagonals1 = set()
diagonals2 = set()

def dfs(n, x):

    if x == n:
        return 1
    
    else:
        count = 0
        for y in range(n):
            if y in columns or (x + y) in diagonals1 or (x - y) in diagonals2:
                continue
            
            columns.add(y)
            diagonals1.add(x + y)
            diagonals2.add(x - y)
            count += dfs(n, x + 1)
            columns.remove(y)
            diagonals1.remove(x + y)
            diagonals2.remove(x - y)

        return count
    
    
def solution(n):
    
    return dfs(n, 0)

if __name__ == "__main__":
    n = 4
    print(solution(n))