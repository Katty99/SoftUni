from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_power = deque(int(x) for x in input().split(', '))

palm_firework = 0
willow_firework = 0
crossette_firework = 0

has_succeeded = False

while firework_effects and explosive_power:
    current_firework = firework_effects.popleft()
    if current_firework <= 0:
        continue
    current_power = explosive_power.pop()
    if current_power <= 0:
        firework_effects.appendleft(current_firework)
        continue

    current_sum = current_firework + current_power

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        palm_firework += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        willow_firework += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette_firework += 1
    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_power)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        has_succeeded = True
        break

if has_succeeded:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")