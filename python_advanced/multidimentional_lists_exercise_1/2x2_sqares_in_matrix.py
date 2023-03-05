rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

number_of_matrices = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        element = matrix[row][col]

        if matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1] == element:
            number_of_matrices += 1

print(number_of_matrices)
