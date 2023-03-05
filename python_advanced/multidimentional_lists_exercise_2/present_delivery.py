number_of_presents = int(input())
size_of_neighbourhood = int(input())
neighbourhood = [[x for x in input().split()] for _ in range(size_of_neighbourhood)]
santa_position = []
naughty_kids = []
nice_kids = []
cookies_positions = []
happy_kids = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(size_of_neighbourhood):
    for col in range(size_of_neighbourhood):
        current_position = neighbourhood[row][col]
        if current_position == 'S':
            santa_position = [row, col]
            neighbourhood[row][col] = '-'
        elif current_position == 'X':
            naughty_kids.append([row, col])
        elif current_position == 'V':
            nice_kids.append([row, col])

while number_of_presents > 0:
    direction = input()
    if direction == 'Christmas morning':
        break
    row_movement = santa_position[0] + directions[direction][0]
    col_movement = santa_position[1] + directions[direction][1]

    if 0 <= row_movement < size_of_neighbourhood and 0 <= col_movement < size_of_neighbourhood:
        santa_position = [row_movement, col_movement]
        if neighbourhood[row_movement][col_movement] == 'C':
            for movement in directions.values():
                if neighbourhood[santa_position[0] + movement[0]][santa_position[1] + movement[1]].isalpha():
                    number_of_presents -= 1
                    if neighbourhood[santa_position[0] + movement[0]][santa_position[1] + movement[1]] == 'V':
                        happy_kids += 1
                        nice_kids.remove([santa_position[0] + movement[0], santa_position[1] + movement[1]])
                    neighbourhood[santa_position[0] + movement[0]][santa_position[1] + movement[1]] = '-'

        elif neighbourhood[row_movement][col_movement] == 'V':
            number_of_presents -= 1
            happy_kids += 1
            neighbourhood[row_movement][col_movement] = '-'
            nice_kids.remove([row_movement, col_movement])

        elif neighbourhood[row_movement][col_movement] == 'X':
            neighbourhood[row_movement][col_movement] = '-'

neighbourhood[santa_position[0]][santa_position[1]] = 'S'

if not number_of_presents and happy_kids < len(nice_kids):
    print('Santa ran out of presents!')
print(*[' '.join(x) for x in neighbourhood], sep='\n')
if len(nice_kids) == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
