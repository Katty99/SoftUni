heroes_spells = {}
while True:
    command = input()
    if command == 'End':
        break
    action = command.split(' ')
    if action[0] == 'Enroll':
        hero_name = action[1]
        if hero_name not in heroes_spells:
            heroes_spells[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif action[0] == 'Learn':
        hero_name = action[1]
        spell = action[2]
        if hero_name not in heroes_spells:
            print(f"{hero_name} doesn't exist.")
        elif spell in heroes_spells[hero_name]:
            print(f"{hero_name} has already learnt {spell}.")
        else:
            heroes_spells[hero_name].append(spell)

    elif action[0] == 'Unlearn':
        hero_name = action[1]
        spell = action[2]
        if hero_name not in heroes_spells:
            print(f"{hero_name} doesn't exist.")
        elif spell not in heroes_spells[hero_name]:
            print(f"{hero_name} doesn't know {spell}.")
        else:
            heroes_spells[hero_name].remove(spell)

print("Heroes:")
for hero, spells in heroes_spells.items():
    print(f"== {hero}: {', '.join(spells)}")