def check_surrounding_numbers(r, c, size):
    current_sum = int(matrix[r][0]) + int(matrix[r][size - 1]) + int(matrix[0][c]) + int(matrix[size - 1][c])
    return int(current_sum)


SIZE = 7
player_1, player_2 = input().split(', ')
matrix = [[x for x in input().split()] for _ in range(SIZE)]

points = {player_1: 501, player_2: 501}

player_throws = {player_1: 0, player_2: 0}

player_1_wins = False
player_2_wins = False

throws = 0

while True:
    throws += 1
    if throws % 2 == 0:
        current_player = player_2
    else:
        current_player = player_1
    player_throws[current_player] += 1

    row, col = input().strip('(').strip(')').split(', ')
    row, col = int(row), int(col)

    if row not in range(SIZE) or col not in range(SIZE):
        continue

    current_target = matrix[row][col]

    if current_target.isdigit():
        points[current_player] -= int(current_target)

    elif current_target == 'D':
        points[current_player] -= check_surrounding_numbers(row, col, SIZE) * 2

    elif current_target == 'T':
        points[current_player] -= check_surrounding_numbers(row, col, SIZE) * 3

    elif current_target == 'B':
        points[current_player] = 0

    if points[current_player] <= 0:
        print(f"{current_player} won the game with {player_throws[current_player]} throws!")
        break
