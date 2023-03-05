def primary_diagonal(matrix):
    first_diagonal = []
    for row in range(rows):
        first_diagonal.append(matrix[row][row])
    return first_diagonal


def secondary_diagonal(matrix, rows):
    second_diagonal = []
    col = rows - 1
    for r in range(0, rows):
        second_diagonal.append(matrix[r][col])
        col -= 1
    return second_diagonal


rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
first_diagonal = primary_diagonal(matrix)
first_sum = sum(first_diagonal)
second_diagonal = secondary_diagonal(matrix, rows)
second_sum = sum(second_diagonal)
print(f"Primary diagonal: {', '.join(str(x) for x in first_diagonal)}. Sum: {first_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {second_sum}")

