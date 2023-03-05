def even_odd_sum(digit):
    even_counter = 0
    odd_counter = 0
    for current_num in digit:
        if int(current_num) % 2 == 0:
            even_counter += int(current_num)
        else:
            odd_counter += int(current_num)
    return f'Odd sum = {odd_counter}, Even sum = {even_counter}'


number = input()
print(even_odd_sum(number))