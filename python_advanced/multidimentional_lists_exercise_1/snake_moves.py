from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = list(input())
snake_copy = deque(snake)

for row in range(rows):
    while len(snake_copy) < columns:
        snake_copy.extend(snake)
    if row % 2 == 0:
        print(*[snake_copy.popleft() for _ in range(columns)], sep='')
    else:
        print(*[snake_copy.popleft() for _ in range(columns)][::-1], sep='')