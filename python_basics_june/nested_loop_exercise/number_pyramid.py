number = int(input())
counter = 1
is_biggest_number = False
for rows in range(1, number + 1):
    for col in range(1, rows + 1):
        print(counter, end=' ')
        counter += 1
        if counter > number:
            is_biggest_number = True
            break
    if is_biggest_number:
        break
    print()