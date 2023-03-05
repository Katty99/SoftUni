from collections import deque

food_quantity = int(input())
orders = deque([int(n) for n in input().split(' ')])
max_order = max(orders)
print(max_order)
for current in orders.copy():
    if current <= food_quantity:
        food_quantity -= current
        orders.popleft()
    else:
        if orders:
            print(f"Orders left: {' '.join([str(o) for o in orders])}")
            break

if not orders:
    print('Orders complete')
