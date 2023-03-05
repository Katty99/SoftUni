from collections import deque

caffeine_mg = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))
total_caffeine = 0
MAXIMUM_CAFFEINE = 300

while caffeine_mg and energy_drinks:
    current_caffeine = caffeine_mg.pop()
    current_energy_drink = energy_drinks.popleft()
    current_drink = current_caffeine * current_energy_drink
    if current_drink + total_caffeine <= MAXIMUM_CAFFEINE:
        total_caffeine += current_drink

    else:
        energy_drinks.append(current_energy_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    to_print = [str(x) for x in energy_drinks]
    print(f"Drinks left: {', '.join(to_print)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")