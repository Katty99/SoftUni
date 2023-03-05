rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

position = []

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'B':
            position = [row, col]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

players_caught = 0
moves_made = 0

while True:
    direction = input()
    if direction == 'Finish':
        break

    next_row = position[0] + directions[direction][0]
    next_col = position[1] + directions[direction][1]

    if next_row not in range(rows) or next_col not in range(cols):
        continue

    if matrix[next_row][next_col] == 'O':
        continue

    moves_made += 1
    position = [next_row, next_col]
    if matrix[position[0]][position[1]] == 'P':
        players_caught += 1
        matrix[position[0]][position[1]] = '-'

    if players_caught == 3:
        break

print("Game over!")
print(f"Touched opponents: {players_caught} Moves made: {moves_made}")