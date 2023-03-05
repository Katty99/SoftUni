field_size = int(input())
matrix = [[x for x in input().split()] for _ in range(field_size)]
bunny_position = []
max_sum = 0
path = []
best_direction = None

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for current_row in range(field_size):
    for current_col in range(field_size):
        if matrix[current_row][current_col] == 'B':
            bunny_position = [current_row, current_col]

for direction, coordinates in directions.items():
    current_sum = 0
    current_path = []
    row = bunny_position[0] + coordinates[0]
    col = bunny_position[1] + coordinates[1]
    while 0 <= row < field_size and 0 <= col < field_size:
        if matrix[row][col] == 'X':
            break
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row += coordinates[0]
        col += coordinates[1]
    if current_sum >= max_sum:
        max_sum = current_sum
        path = current_path
        best_direction = direction

print(best_direction)
print(*path, sep='\n')
print(max_sum)

