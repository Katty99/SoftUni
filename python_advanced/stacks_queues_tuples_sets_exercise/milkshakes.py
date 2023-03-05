from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes_count = 0

while milkshakes_count < 5 and chocolates and cups_of_milk:
    current_chocolate = chocolates.pop()
    current_milk = cups_of_milk.popleft()
    if current_milk <= 0 and current_chocolate <= 0:
        continue
    elif current_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
        continue

    if current_milk == current_chocolate:
        milkshakes_count += 1
    elif current_milk != current_chocolate:
        cups_of_milk.append(current_milk)
        chocolates.append(current_chocolate - 5)

if milkshakes_count >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
