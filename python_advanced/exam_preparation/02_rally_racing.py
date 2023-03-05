size = int(input())
racing_number = input()
race_route = [[x for x in input().split()] for _ in range(size)]
car_position = [0, 0]
finish_line_position = []
tunnel_position = []


for row in range(size):
    for col in range(size):
        if race_route[row][col] == 'T':
            tunnel_position.append([row, col])
        elif race_route[row][col] == 'F':
            finish_line_position = [row, col]

tunnel_entry = tunnel_position[0]
tunnel_exit = tunnel_position[1]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

has_finished = False
kilometers_passed = 0

while True:
    direction = input()
    if direction == 'End':
        break

    car_position[0] += directions[direction][0]
    car_position[1] += directions[direction][1]
    kilometers_passed += 10

    if car_position == tunnel_entry:
        race_route[tunnel_entry[0]][tunnel_entry[1]] = '.'
        race_route[tunnel_exit[0]][tunnel_exit[1]] = '.'
        car_position = tunnel_exit.copy()
        kilometers_passed += 20

    elif car_position == tunnel_exit:
        race_route[tunnel_exit[0]][tunnel_exit[1]] = '.'
        race_route[tunnel_entry[0]][tunnel_entry[1]] = '.'
        car_position = tunnel_entry.copy()
        kilometers_passed += 20

    if car_position == finish_line_position:
        has_finished = True
        break


race_route[car_position[0]][car_position[1]] = 'C'

if has_finished:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {kilometers_passed} km.")
print(*[''.join(element) for element in race_route], sep='\n')
