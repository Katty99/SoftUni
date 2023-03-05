size = int(input())
battlefield = [[row for row in input()] for _ in range(size)]
submarine_position = []

for row in range(size):
    for col in range(size):
        if battlefield[row][col] == 'S':
            submarine_position = [row, col]
            battlefield[row][col] = '-'

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

damage = 0
cruisers_destroyed = 0

while True:
    if damage == 3:
        break
    if cruisers_destroyed == 3:
        break
    command = input()

    submarine_position[0] += directions[command][0]
    submarine_position[1] += directions[command][1]

    if size <= submarine_position[0] < 0 and size <= submarine_position[1] < 0:
        continue

    if battlefield[submarine_position[0]][submarine_position[1]] == 'C':
        cruisers_destroyed += 1

    elif battlefield[submarine_position[0]][submarine_position[1]] == '*':
        damage += 1

    battlefield[submarine_position[0]][submarine_position[1]] = '-'
battlefield[submarine_position[0]][submarine_position[1]] = 'S'

if damage == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_position}!")

elif cruisers_destroyed == 3:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

print(*[''.join(element) for element in battlefield], sep='\n')