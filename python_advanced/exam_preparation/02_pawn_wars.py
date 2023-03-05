def check_capture(attacker_position, defender_position):
    a_row = attacker_position[0]
    a_col = attacker_position[1]
    d_row = defender_position[0]
    d_col = defender_position[1]
    if a_row - 1 >= 0 and a_col - 1 >= 0:
        if a_row - 1 == d_row and a_col - 1 == d_col:
            return [a_row - 1, a_col - 1]
    if a_row - 1 >= 0 and a_col + 1 < 8:
        if a_row - 1 == d_row and a_col + 1 == d_col:
            return [a_row - 1, a_col + 1]
    if a_row + 1 < 8 and a_col - 1 >= 0:
        if a_row + 1 == d_row and a_col - 1 == d_col:
            return [a_row + 1, a_col - 1]
    if a_row + 1 < 8 and a_col + 1 < 8:
        if a_row + 1 == d_row and a_col + 1 == d_col:
            return [a_row + 1, a_col + 1]


SIZE = 8
board = [[x for x in input().split()] for _ in range(SIZE)]

white_position = []
black_position = []

for row in range(SIZE):
    for col in range(SIZE):
        if board[row][col] == 'w':
            white_position = [row, col]
        elif board[row][col] == 'b':
            black_position = [row, col]

white_movement = [-1, 0]
black_movement = [1, 0]

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for _ in range(SIZE):
    # Checking White first
    capture_check = check_capture(white_position, black_position)
    if capture_check:
        square = [positions_col[capture_check[1]], position_row[capture_check[0]]]
        print(f"Game over! White win, capture on {''.join(str(x) for x in square)}.")
        break
    white_position[0] += white_movement[0]
    if white_position[0] == 0:
        position = [positions_col[white_position[1]], position_row[white_position[0]]]
        print(f"Game over! White pawn is promoted to a queen at {''.join(str(x) for x in position)}.")
        break

    # After that, checking Black
    capture_check = check_capture(black_position, white_position)
    if capture_check:
        square = [positions_col[capture_check[1]], position_row[capture_check[0]]]
        print(f"Game over! Black win, capture on {''.join(str(x) for x in square)}.")
        break
    black_position[0] += black_movement[0]
    if black_position[0] == 7:
        position = [positions_col[black_position[1]], position_row[black_position[0]]]
        print(f"Game over! Black pawn is promoted to a queen at {''.join(str(x) for x in position)}.")
        break

