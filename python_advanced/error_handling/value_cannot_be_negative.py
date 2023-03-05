class ValueCannotBeNegative(Exception):
    pass


numbers = [int(input()) for _ in range(6) if _ > 0]

for num in numbers:
    if num < 0:
        raise ValueCannotBeNegative