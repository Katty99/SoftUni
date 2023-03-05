command = input()
games_played = 0
win_counter = 0
lose_counter = 0
while command != 'End of tournaments':
    number_of_tournaments = int(input())
    games_played += number_of_tournaments
    for game in range(1, number_of_tournaments + 1):
        home_score = int(input())
        guest_score = int(input())
        difference = abs(home_score - guest_score)
        if home_score > guest_score:
            win_counter += 1
            print(f'Game {game} of tournament {command}: win with {difference} points.')
        else:
            lose_counter += 1
            print(f'Game {game} of tournament {command}: lost with {difference} points.')
    command = input()

lose_percent = lose_counter / games_played * 100
win_percent = win_counter / games_played * 100

print(f'{win_percent:.2f}% matches win')
print(f'{lose_percent:.2f}% matches lost')



