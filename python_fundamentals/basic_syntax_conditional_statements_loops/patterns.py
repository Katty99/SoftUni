rows = int(input())
for i in range(1, rows + 1):
    print(i * '*')
for j in range(rows - 1, -1, -1):
    print(j * '*')