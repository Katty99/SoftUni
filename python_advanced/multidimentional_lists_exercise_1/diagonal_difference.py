rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for r in range(rows):
    primary_diagonal.append(matrix[r][r])

cols = rows - 1
for r in range(0, rows):
    secondary_diagonal.append(matrix[r][cols])
    cols -= 1
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))