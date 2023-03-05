from collections import deque

eggs_sizes = deque(int(x) for x in input().split(', '))
paper_sizes = deque(int(x) for x in input().split(', '))

SIZE = 50
boxes_filled = 0

while eggs_sizes and paper_sizes:
    current_egg = eggs_sizes.popleft()

    if current_egg <= 0:
        continue
    elif current_egg == 13:
        first_paper = paper_sizes.popleft()
        last_paper = paper_sizes.pop()
        paper_sizes.appendleft(last_paper)
        paper_sizes.append(first_paper)
        continue

    current_paper = paper_sizes.pop()
    current_sum = current_egg + current_paper
    if current_sum <= 50:
        boxes_filled += 1

if boxes_filled:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_sizes)}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")


