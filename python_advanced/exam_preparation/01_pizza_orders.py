from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employees = deque(int(x) for x in input().split(', '))

completed_orders = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    if current_order > 10 or current_order <= 0:
        continue

    current_employee = employees.pop()
    if current_order <= current_employee:
        completed_orders += current_order
    else:
        current_order -= current_employee
        completed_orders += current_employee
        pizza_orders.appendleft(current_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {completed_orders}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
