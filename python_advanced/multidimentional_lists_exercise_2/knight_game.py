size = int(input())
matrix = [list(input()) for _ in range(size)]

directions = (
    (-2, 1),
    (-2, -1),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
)

removed_knights = 0

while True:
    knight_with_most_attacks_position = []
    max_attacks = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0
                for direction in directions:
                    current_row = row + direction[0]
                    current_col = col + direction[1]
                    if 0 <= current_row < len(matrix) and 0 <= current_col < len(matrix[row]):
                        if matrix[current_row][current_col] == 'K':
                            attacks += 1
                if attacks > max_attacks:
                    knight_with_most_attacks_position = [row, col]
                    max_attacks = attacks
    if knight_with_most_attacks_position:
        r, c = knight_with_most_attacks_position
        matrix[r][c] = 0
        removed_knights += 1
    else:
        break
print(removed_knights)