lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmets_broken = lost_fights // 2
swords_broken = lost_fights // 3
shields_broken = lost_fights // 6
armors_broken = shields_broken // 2
expenses = helmet_price * helmets_broken + \
           sword_price * swords_broken + \
           shield_price * shields_broken + \
           armor_price * armors_broken
print(f'Gladiator expenses: {expenses:.2f} aureus')
