rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for y in range(rows)]
for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_sum += int(matrix[row][col])
    print(current_sum)
