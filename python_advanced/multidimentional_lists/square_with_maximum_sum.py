rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
largest_sum = float("-inf")
largest_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        first_row = matrix[row][col:col + 2]
        second_row = matrix[row + 1][col:col + 2]
        current_sum = sum(first_row) + sum(second_row)
        if current_sum > largest_sum:
            largest_sum = current_sum
            largest_matrix = [first_row, second_row]
[print(*largest_matrix[row]) for row in range(2)]
print(largest_sum)
