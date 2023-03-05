from math import floor

number_of_tournaments = int(input())
initial_points = int(input())
total_points = initial_points
number_of_tournaments_won = 0
for i in range(1, number_of_tournaments + 1):
    tournament_phase = input()
    if tournament_phase == 'W':
        total_points += 2000
        number_of_tournaments_won += 1
    elif tournament_phase == 'F':
        total_points += 1200
    elif tournament_phase == 'SF':
        total_points += 720
average_points = (total_points - initial_points) / number_of_tournaments
percentage_tournaments_won = (number_of_tournaments_won / number_of_tournaments) * 100
print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percentage_tournaments_won:.2f}%')
