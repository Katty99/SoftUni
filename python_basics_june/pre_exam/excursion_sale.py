number_of_sea_excursions = int(input())
number_of_mountain_excursions = int(input())
profit = 0

while number_of_mountain_excursions > 0 or number_of_sea_excursions > 0:
    command = input()
    if command == 'sea':
        number_of_sea_excursions -= 1
        if number_of_sea_excursions < 0:
            current_sea_profit = 0
        else:
            current_sea_profit = 680
        profit += current_sea_profit
    elif command == 'mountain':
        number_of_mountain_excursions -= 1
        if number_of_mountain_excursions < 0:
            current_mountain_profit = 0
        else:
            current_mountain_profit = 499
        profit += current_mountain_profit
    elif command == 'Stop':
        break
if number_of_sea_excursions <= 0 and number_of_mountain_excursions <= 0:
    print(f'Good job! Everything is sold.')
    print(f'Profit: {profit} leva.')
else:
    print(f'Profit: {profit} leva.')