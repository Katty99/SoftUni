group_size = int(input())
number_of_days = int(input())
coins_counter = 0
for current_day in range(1, number_of_days + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 3 == 0:
        coins_counter -= 3 * group_size
    if current_day % 5 == 0:
        coins_counter += 20 * group_size
        if current_day % 3 == 0:
            coins_counter -= 2 * group_size
    coins_counter += 50
    coins_counter -= 2 * group_size
coins_per_companion = int(coins_counter / group_size)
print(f'{group_size} companions received {coins_per_companion} coins each.')

