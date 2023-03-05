SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]

position = input()
my_position = []
for symbol in position:
    if symbol.isdigit():
        my_position.append(int(symbol))

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    command = input().split(', ')
    if 'Stop' in command:
        break

    direction = command[1]
    my_position[0] += directions[direction][0]
    my_position[1] += directions[direction][1]

    if 'Create' in command:
        if matrix[my_position[0]][my_position[1]] == '.':
            matrix[my_position[0]][my_position[1]] = command[2]

    elif 'Update' in command:
        if matrix[my_position[0]][my_position[1]] != '.':
            matrix[my_position[0]][my_position[1]] = command[2]

    elif 'Read' in command:
        if matrix[my_position[0]][my_position[1]] != '.':
            print(matrix[my_position[0]][my_position[1]])

    elif 'Delete' in command:
        if matrix[my_position[0]][my_position[1]] != '.':
            matrix[my_position[0]][my_position[1]] = '.'

print(*[' '.join(row) for row in matrix], sep='\n')