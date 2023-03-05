initial_energy = int(input())
won_battles = 0
has_failed = False
while True:
    command = input()
    if command == 'End of battle':
        break
    else:
        command = int(command)
        if command <= initial_energy:
            initial_energy -= command
            won_battles += 1
            if won_battles % 3 == 0:
                initial_energy += won_battles
        elif command > initial_energy:
            has_failed = True
            break
if has_failed:
    print(f'Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy')
else:
    print(f'Won battles: {won_battles}. Energy left: {initial_energy}')