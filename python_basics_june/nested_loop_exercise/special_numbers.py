number = int(input())

for current_number in range(1111, 10000):
    is_special = True
    current_num_to_str = str(current_number)
    for current_digit in current_num_to_str:
        if int(current_digit) == 0 or number % int(current_digit) !=0:
            is_special = False
            break
    if is_special:
        print(current_num_to_str, end=' ')
print()


