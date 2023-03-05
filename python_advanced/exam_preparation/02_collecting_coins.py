size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]
position = []
path = []

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'P':
            position = [r, c]
            path.append([r, c])

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

game_won = False
coins = 0

while not game_won:
    direction = input()
    if direction not in ['up', 'down', 'left', 'right']:
        continue

    matrix[position[0]][position[1]] = '0'
    position[0] += directions[direction][0]
    position[1] += directions[direction][1]

    if position[0] < 0:
        position[0] = size - 1
    elif position[0] == size:
        position[0] = 0

    if position[1] < 0:
        position[1] = size - 1
    elif position[1] == size:
        position[1] = 0

    path.append([position[0], position[1]])

    current_position = matrix[position[0]][position[1]]

    if current_position == 'X':
        coins = int(coins / 2)
        break
    elif str(current_position).isnumeric():
        coins += int(current_position)

    matrix[position[0]][position[1]] = '0'

    if coins >= 100:
        game_won = True
        break

if game_won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
[print(el) for el in path]
