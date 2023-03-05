from collections import deque

ramen_bowls = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while ramen_bowls and customers:
    current_bowl = ramen_bowls.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        current_bowl -= current_customer
        ramen_bowls.append(current_bowl)

    elif current_bowl < current_customer:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")