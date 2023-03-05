rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for r in range(rows):
    matrix.append(list(int(x) for x in input().split(', ')))

total = sum([sum(x) for x in matrix])
print(total)
print(matrix)
