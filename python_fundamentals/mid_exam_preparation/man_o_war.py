pirate_ship_status = [int(y) for y in input().split('>')]
warship_status = [int(x) for x in input().split('>')]
maximum_capacity = int(input())
has_sunken = False
while True:
    command = input().split()
    if command[0] == 'Retire':
        break
    elif command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if index >= len(warship_status) or index < 0:
            continue
        else:
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                has_sunken = True
                print('You won! The enemy ship has sunken.')
                break
    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        current_damage = int(command[3])
        if start_index < 0 or start_index >= len(pirate_ship_status) \
                or end_index < 0 or end_index >= len(pirate_ship_status) or current_damage <= 0:
            continue
        else:
            for current_index in range(start_index, end_index + 1):
                pirate_ship_status[current_index] -= current_damage
                if pirate_ship_status[current_index] <= 0:
                    has_sunken = True
            if has_sunken:
                print('You lost! The pirate ship has sunken.')
                break
    elif command[0] == 'Repair':
        idx = int(command[1])
        health = int(command[2])
        if idx < 0 or idx >= len(pirate_ship_status):
            continue
        else:
            pirate_ship_status[idx] += health
            if pirate_ship_status[idx] > maximum_capacity:
                pirate_ship_status[idx] = maximum_capacity
    elif command[0] == 'Status':
        counter = 0
        for current_section in pirate_ship_status:
            if current_section < maximum_capacity * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')
if not has_sunken:
    print(f'Pirate ship status: {sum(pirate_ship_status)}')
    print(f'Warship status: {sum(warship_status)}')