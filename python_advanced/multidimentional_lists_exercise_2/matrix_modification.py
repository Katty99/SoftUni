matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
while True:
    command = input()
    if command == 'END':
        [print(*matrix[row]) for row in range(len(matrix))]
        break
    action, row, col, value = [int(x) if x.isdigit() else x for x in command.split()]
    if 0 <= int(row) < len(matrix) and 0 <= int(col) < len(matrix[0]):
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
