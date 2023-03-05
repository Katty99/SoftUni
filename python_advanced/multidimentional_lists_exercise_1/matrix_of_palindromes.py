rows, cols = [int(x) for x in input().split()]
matrix = []

for r in range(rows):
    first_letter = 97 + r
    third_letter = first_letter
    current_row = []
    for c in range(cols):
        second_letter = first_letter + c
        current_string = chr(first_letter) + chr(second_letter) + chr(third_letter)
        current_row.append(current_string)
    matrix.append(current_row)

[print(*matrix[row]) for row in range(rows)]
