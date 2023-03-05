size = 5
matrix = [[x for x in input().split()] for _ in range(size)]

current_position = []
targets_shot = []
targets_shot_counter = 0
number_of_targets = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'A':
            current_position = [row, col]
        elif matrix[row][col] == 'x':
            number_of_targets += 1

number_of_commands = int(input())
for current_command in range(number_of_commands):
    command = input().split()

    if command[0] == 'move':
        direction = command[1]
        steps = int(command[2])
        row_movement = current_position[0] + directions[direction][0] * steps
        col_movement = current_position[1] + directions[direction][1] * steps

        if 0 <= row_movement < size and 0 <= col_movement < size and matrix[row_movement][col_movement] == '.':
            matrix[current_position[0]][current_position[1]] = '.'
            current_position = [row_movement, col_movement]
            matrix[current_position[0]][current_position[1]] = 'A'

    elif command[0] == 'shoot':
        direction = command[1]
        row_movement = current_position[0] + directions[direction][0]
        col_movement = current_position[1] + directions[direction][1]
        while 0 <= row_movement < size and 0 <= col_movement < size:
            if matrix[row_movement][col_movement] == 'x':
                targets_shot.append([row_movement, col_movement])
                targets_shot_counter += 1
                matrix[row_movement][col_movement] = '.'
                break
            row_movement += directions[direction][0]
            col_movement += directions[direction][1]
    if targets_shot_counter == number_of_targets:
        break


if targets_shot_counter == number_of_targets:
    print(f"Training completed! All {number_of_targets} targets hit.")
else:
    print(f"Training not completed! {number_of_targets - targets_shot_counter} targets left.")

print(*targets_shot, sep='\n')