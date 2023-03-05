SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]

rover_position = []
for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == "E":
            rover_position = [row, col]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

water = 0
metal = 0
concrete = 0

commands = input().split(', ')
for direction in commands:
    rover_position[0] += directions[direction][0]
    rover_position[1] += directions[direction][1]

    if rover_position[0] < 0:
        rover_position[0] = 5
    elif rover_position[0] > 5:
        rover_position[0] = 0

    if rover_position[1] < 0:
        rover_position[1] = 5
    elif rover_position[1] > 5:
        rover_position[1] = 0

    current_row = rover_position[0]
    current_col = rover_position[1]
    if matrix[current_row][current_col] == 'W':
        water += 1
        print(f"Water deposit found at ({current_row}, {current_col})")

    elif matrix[current_row][current_col] == 'M':
        metal += 1
        print(f"Metal deposit found at ({current_row}, {current_col})")

    elif matrix[current_row][current_col] == 'C':
        concrete += 1
        print(f"Concrete deposit found at ({current_row}, {current_col})")

    elif matrix[current_row][current_col] == 'R':
        print(f"Rover got broken at ({current_row}, {current_col})")
        break

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")