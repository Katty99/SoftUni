bottles_of_detergent = int(input())
ml_of_detergent = bottles_of_detergent * 750
ml_detergent_counter = 0
number_of_loads = 0
number_of_dishes = 0
number_of_pots = 0

while ml_detergent_counter <= ml_of_detergent:
    command = input()
    if command != 'End':
        items = int(command)
        number_of_loads += 1
        if number_of_loads % 3 == 0:
            number_of_pots += items
            ml_detergent_counter += items * 15
        else:
            number_of_dishes += items
            ml_detergent_counter += items * 5
    else:
        break
difference = abs(ml_detergent_counter - ml_of_detergent)
if ml_detergent_counter <= ml_of_detergent:
    print(f'Detergent was enough!')
    print(f'{number_of_dishes} dishes and {number_of_pots} pots were washed.')
    print(f'Leftover detergent {difference} ml.')
else:
    print(f'Not enough detergent, {difference} ml. more necessary!')