rows, cols = [int(x) for x in input().split(', ')]
matrix = [[x for x in input().split()] for _ in range(rows)]
initial_position = []

decorations_count = 0
gifts_count = 0
cookies_count = 0

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'Y':
            matrix[row][col] = 'x'
            initial_position = [row, col]
        elif matrix[row][col] == 'D':
            decorations_count += 1
        elif matrix[row][col] == 'G':
            gifts_count += 1
        elif matrix[row][col] == 'C':
            cookies_count += 1

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

decorations = 0
gifts = 0
cookies = 0
everything_is_collected = False

while not everything_is_collected:
    command = input()
    if command == 'End':
        break

    direction, steps = command.split('-')
    steps = int(steps)

    for current in range(0, steps):

        matrix[initial_position[0]][initial_position[1]] = 'x'

        next_row = initial_position[0] + directions[direction][0]
        next_col = initial_position[1] + directions[direction][1]

        if next_row < 0:
            next_row = rows - 1
        elif next_row == rows:
            next_row = 0

        if next_col < 0:
            next_col = cols - 1
        elif next_col == cols:
            next_col = 0

        if matrix[next_row][next_col] == 'D':
            decorations += 1
        elif matrix[next_row][next_col] == 'G':
            gifts += 1
        elif matrix[next_row][next_col] == 'C':
            cookies += 1

        initial_position = [next_row, next_col]
        matrix[initial_position[0]][initial_position[1]] = 'Y'

        if decorations == decorations_count and gifts == gifts_count and cookies == cookies_count:
            everything_is_collected = True
            break


if everything_is_collected:
    print("Merry Christmas!")
print("You've collected:")
print(f'- {decorations} Christmas decorations')
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

print(*[' '.join(row) for row in matrix], sep='\n')