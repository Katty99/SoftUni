def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return f'Enter valid values!'
    area = length * width
    perimeter = 2 * length + 2 * width
    return f'''Rectangle area: {area}
Rectangle perimeter: {perimeter}'''


print(rectangle(2, 10))