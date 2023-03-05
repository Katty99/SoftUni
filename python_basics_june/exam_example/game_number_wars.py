name_player_one = input()
name_player_two = input()
points_player_1 = 0
points_player_2 = 0
while True:
    command = input()
    if command == 'End of game':
        print(f'{name_player_one} has {points_player_1} points')
        print(f'{name_player_two} has {points_player_2} points')
        break
    card1 = int(command)
    card2 = int(input())
    points = abs(card1 - card2)
    if card1 > card2:
        points_player_1 += points
    elif card1 < card2:
        points_player_2 += points
    elif card1 == card2:
        print(f'Number wars!')
        card1 = int(input())
        card2 = int(input())
        if points_player_1 > points_player_2:
            print(f'{name_player_one} is winner with {points_player_1} points')
        else:
            print(f'{name_player_two} is winner with {points_player_2} points')
        break


