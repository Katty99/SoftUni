SIZE = 6
matrix = [[x for x in input().split()] for _ in range(SIZE)]

prizes = {
    'Football': [100, 200],
    'Teddy Bear': [200, 300],
    'Lego Construction Set': [300]
}

buckets_hit = []
total_points = 0

THROWS = 3
for throw in range(THROWS):
    coordinates = input()
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    row, col = coordinates.split(', ')
    row = int(row)
    col = int(col)
    if 0 <= row < SIZE and 0 <= col < SIZE:
        if matrix[row][col] == 'B' and [row, col] not in buckets_hit:
            buckets_hit.append([row, col])
            for current_row in range(SIZE):
                if matrix[current_row][col].isdigit():
                    total_points += int(matrix[current_row][col])

success = False

for key, value in prizes.items():
    if len(value) == 2:
        if value[0] <= total_points < value[1]:
            success = True
    else:
        if total_points >= value[0]:
            success = True
    if success:
        print(f"Good job! You scored {total_points} points, and you've won {key}.")
        break

if not success:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")