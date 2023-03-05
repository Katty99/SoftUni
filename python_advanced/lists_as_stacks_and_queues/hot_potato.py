from collections import deque
kids = deque(input().split(' '))
toss = int(input())
counter = 1
while len(kids) > 1:
    if counter == toss:
        print(f'Removed {kids.popleft()}')
        counter = 1
    else:
        kids.append(kids.popleft())
        counter += 1

print(f'Last is {kids.popleft()}')