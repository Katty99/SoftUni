matrix = [[x for x in input()] for _ in range(int(input()))]
searched_symbol = input()
coordinates = []
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        current_element = matrix[r][c]
        if current_element == searched_symbol:
            coordinates.append(r)
            coordinates.append(c)
            break
if coordinates:
    print(f"({coordinates[0]}, {coordinates[1]})")
else:
    print(f"{searched_symbol} does not occur in the matrix")
