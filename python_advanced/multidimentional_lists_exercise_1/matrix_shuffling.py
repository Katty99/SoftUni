rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    if len(command.split()) == 5:
        action, row_1, col_1, row_2, col_2 = [int(x) if x.isdigit() else x for x in command.split()]
        if action == 'swap' and 0 <= row_1 <= rows and 0 <= row_2 <= rows and 0 <= col_1 <= cols and 0 <= col_2 <= cols:
            first_symbol = matrix[row_1][col_1]
            second_symbol = matrix[row_2][col_2]
            matrix[row_1][col_1] = second_symbol
            matrix[row_2][col_2] = first_symbol
            [print(*matrix[row]) for row in range(rows)]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
