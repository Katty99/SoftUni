names_order = input().split(', ')

SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]

first_has_to_rest = False
second_has_to_rest = False

while True:
    first_player_coordinates = input()
    first_player_coordinates_list = [int(first_player_coordinates[1]), int(first_player_coordinates[4])]
    if not first_has_to_rest:
        first_position = matrix[first_player_coordinates_list[0]][first_player_coordinates_list[1]]
        if first_position == 'E':
            print(f"{names_order[0]} found the Exit and wins the game!")
            break

        elif first_position == 'T':
            print(f"{names_order[0]} is out of the game! The winner is {names_order[1]}.")
            break

        elif first_position == 'W':
            print(f"{names_order[0]} hits a wall and needs to rest.")
            first_has_to_rest = True
    else:
        first_has_to_rest = False

    second_player_coordinates = input()
    second_player_coordinates_list = [int(second_player_coordinates[1]), int(second_player_coordinates[4])]
    if not second_has_to_rest:
        second_position = matrix[second_player_coordinates_list[0]][second_player_coordinates_list[1]]
        if second_position == 'E':
            print(f"{names_order[1]} found the Exit and wins the game!")
            break

        elif second_position == 'T':
            print(f"{names_order[1]} is out of the game! The winner is {names_order[0]}.")
            break

        elif second_position == 'W':
            print(f"{names_order[1]} hits a wall and needs to rest.")
            second_has_to_rest = True
    else:
        second_has_to_rest = False


