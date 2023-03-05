def rhombus(size):
    to_print = []
    for x in range(size):
        spaces = (size - x - 1) * ' '
        stars = (x + 1) * '* '
        to_print.append([spaces, stars])
    for y in range(size, 1, -1):
        spaces = (size - y + 1) * ' '
        stars = (y - 1) * '* '
        to_print.append([spaces, stars])
    return "\n".join(["".join(map(str, x)) for x in to_print])


rhombus_size = int(input())
print(rhombus(rhombus_size))