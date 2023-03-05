rows = int(input())
matrix = []
final = []
i = 0
for current in range(rows):
    matrix.append(list(int(x) for x in input().split(', ')))
for row in matrix:
    final.append([])
    for el in row:
        if el % 2 == 0:
            final[i].append(el)
    i += 1
print(final)

