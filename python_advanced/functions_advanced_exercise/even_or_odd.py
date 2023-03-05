def even_odd(*args):
    digits = []
    result = []
    command = ''
    for arg in args:
        digits.append(arg)
    command = digits.pop()
    for digit in digits:
        if command == 'even' and digit % 2 == 0:
            result.append(digit)
        elif command == 'odd' and digit % 2 == 1:
            result.append(digit)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "odd"))