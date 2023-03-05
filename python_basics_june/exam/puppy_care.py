food_kg = int(input())
food_gr = food_kg * 1000
total_quantity = 0
while True:
    command = input()
    if command != 'Adopted':
        portion_size = int(command)
        total_quantity += portion_size
    else:
        break

difference = abs(total_quantity - food_gr)
if total_quantity <= food_gr:
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    print(f'Food is not enough. You need {difference} grams more.')
