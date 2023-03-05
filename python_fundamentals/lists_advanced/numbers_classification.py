def positive(number):
    return [num for num in number if int(num) >= 0]


def negative(number):
    return [num for num in number if int(num) < 0]


def even(number):
    return [num for num in number if int(num) % 2 == 0]


def odd(number):
    return [num for num in number if int(num) % 2 != 0]


numbers_list = input().split(', ')
print(f'Positive: {", ".join(positive(numbers_list))}')
print(f'Negative: {", ".join(negative(numbers_list))}')
print(f'Even: {", ".join(even(numbers_list))}')
print(f'Odd: {", ".join(odd(numbers_list))}')
