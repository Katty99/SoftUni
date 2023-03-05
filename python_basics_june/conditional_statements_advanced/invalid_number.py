x = int(input())

valid = 100 <= x <= 200 or x == 0
if not valid:
    print('invalid')

