number_of_heroes = int(input())
heroes_dictionary = {}

for current_hero in range(number_of_heroes):
    hero_name, hp, mp = input().split(' ')
    hp = int(hp)
    mp = int(mp)
    heroes_dictionary[hero_name] = [hp, mp]

while True:
    command = input()
    if command == 'End':
        break

    if 'CastSpell' in command:
        cast_spell, hero_name, mp, spell_name = command.split(' - ')
        mp = int(mp)
        if heroes_dictionary[hero_name][1] >= mp:
            heroes_dictionary[hero_name][1] -= mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif 'TakeDamage' in command:
        take_damage, hero_name, damage, attacker = command.split(' - ')
        damage = int(damage)
        heroes_dictionary[hero_name][0] -= damage
        if heroes_dictionary[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[hero_name][0]}"
                  f" HP left!")
        else:
            heroes_dictionary.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif 'Recharge' in command:
        recharge, hero_name, amount = command.split(' - ')
        amount = int(amount)
        if heroes_dictionary[hero_name][1] + amount > 200:
            amount = 200 - heroes_dictionary[hero_name][1]
        heroes_dictionary[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif 'Heal' in command:
        heal, hero_name, amount = command.split(' - ')
        amount = int(amount)
        if heroes_dictionary[hero_name][0] + amount > 100:
            amount = 100 - heroes_dictionary[hero_name][0]
        heroes_dictionary[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")

for key, value in heroes_dictionary.items():
    print(f"{key}\n  HP: {value[0]}\n  MP: {value[1]}")
