work_events = input().split('|')
initial_energy = 100
coins = 100
earned_coins = 0
is_unsuccessful = False
for current_event in work_events:
    separated = current_event.split('-')
    event = separated[0]
    energy_coins = int(separated[1])
    if event == 'rest':
        if initial_energy == 100:
            print('You gained 0 energy.')
            print(f'Current energy: {initial_energy}.')
        else:
            initial_energy += energy_coins
            print(f'You gained {energy_coins} energy.')
            print(f'Current energy: {initial_energy}.')
    elif event == 'order':
        if initial_energy >= 30:
            earned_coins += energy_coins
            coins += energy_coins
            initial_energy -= 30
            print(f'You earned {energy_coins} coins.')
        else:
            initial_energy += 50
            print('You had to rest!')
            continue
    else:
        if energy_coins >= coins:
            is_unsuccessful = True
            print(f'Closed! Cannot afford {event}.')
            break
        else:
            coins -= energy_coins
            print(f'You bought {event}.')

if not is_unsuccessful:
    print("Day completed!")
    print(f"Coins: {earned_coins}")
    print(f"Energy: {initial_energy}")
