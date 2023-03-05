matrix = [[int(y) for y in input().split(', ')] for x in range(int(input()))]
final = []
for row in matrix:
    for col in row:
        final.append(col)
print(final)