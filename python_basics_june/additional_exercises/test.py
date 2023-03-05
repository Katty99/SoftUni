number_of_days = int(input())
command = input()
total_money = 0
days_won = 0
days_lost = 0

for current_day in range(number_of_days):
    current_money = 0
    win_counter = 0
    lose_counter = 0
    while True:
        result = input()
        if command == 'Finish':
            break
        if result == 'win':
            current_money += 20
            win_counter += 1
        elif result == 'lose':
            lose_counter += 1
        command = input()
    if win_counter > lose_counter:
        current_money += current_money * 10 / 100
        days_won += 1
    else:
        days_lost += 1
        total_money += current_money
    command = input()
if days_won > days_lost:
    total_money += total_money * 20 / 100
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')