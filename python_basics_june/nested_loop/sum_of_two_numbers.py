beginning = int(input())
end = int(input())
magic_number = int(input())
combination = 0
is_found = False
for x in range(beginning, end + 1):
    for y in range(beginning, end + 1):
        combination += 1
        if x + y == magic_number:
            print(f'Combination N:{combination} ({x} + {y} = {magic_number})')
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f'{combination} combinations - neither equals {magic_number}')


