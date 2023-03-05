from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)

while queue:
    command = input()
    if command == 'End':
        break
    if 'refill' in command:
        refill, liters = command.split(' ')
        liters = int(liters)
        water_quantity += liters
    else:
        liters = int(command)
        if liters <= water_quantity:
            print(f"{queue.popleft()} got water")
            water_quantity -= liters
        else:
            print(f"{queue.popleft()} must wait")

print(f"{water_quantity} liters left")