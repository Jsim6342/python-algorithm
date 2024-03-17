from collections import deque

N, M = map(int, input().split())
books = list(map(int, input().split()))
ans = 0
memory = []

left_books = []
right_books = []
for book in books:
    if book < 0:
        left_books.append(book)
    else:
        right_books.append(book)

left_books.sort()
left_books = deque(left_books)
right_books.sort(reverse=True)
right_books = deque(right_books)

while left_books:
    for i in range(M):
        if left_books and i == 0:
            dis = abs(left_books.popleft())
            memory.append(dis)
            ans += dis * 2
        elif left_books:
            left_books.popleft()
        

while right_books:
    for i in range(M):
        if right_books and i == 0:
            dis = right_books.popleft()
            memory.append(dis)
            ans += dis * 2
        elif right_books:
            right_books.popleft()

print(ans-max(memory))


