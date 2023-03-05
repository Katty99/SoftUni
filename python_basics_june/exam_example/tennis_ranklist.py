from math import floor
number_of_tournaments = int(input())
initial_points = int(input())
total_points = 0
win_counter = 0
for current_tournament in range(number_of_tournaments):
    final_position = input()
    if final_position == 'W':
        win_counter += 1
        total_points += 2000
    elif final_position == 'F':
        total_points += 1200
    else:
        total_points += 720
sum_total = initial_points + total_points
average_points = total_points / number_of_tournaments
percentage_won = win_counter / number_of_tournaments * 100
print(f'Final points: {sum_total}')
print(f'Average points: {floor(average_points)}')
print(f'{percentage_won:.2f}%')