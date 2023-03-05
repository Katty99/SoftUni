territory = int(input())
matrix = [[x for x in input().split()] for _ in range(territory)]

alice_position = []
tea_bags = 0
has_succeeded = False

commands = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(territory):
    for col in range(territory):
        if matrix[row][col] == 'A':
            alice_position = [row, col]
            matrix[row][col] = '*'

while True:
    if tea_bags >= 10:
        has_succeeded = True
        break
    command = input()
    current_position = [alice_position[0], alice_position[1]]
    current_position[0] += commands[command][0]
    current_position[1] += commands[command][1]
    if territory <= current_position[0] or territory <= current_position[1] or current_position[0] < 0 \
            or current_position[1] < 0:
        break
    if matrix[current_position[0]][current_position[1]] == 'R':
        matrix[current_position[0]][current_position[1]] = '*'
        break
    if matrix[current_position[0]][current_position[1]].isdigit():
        tea_bags += int(matrix[current_position[0]][current_position[1]])

    matrix[current_position[0]][current_position[1]] = '*'
    alice_position = [current_position[0], current_position[1]]

if has_succeeded:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
print(*[' '.join(element) for element in matrix], sep='\n')