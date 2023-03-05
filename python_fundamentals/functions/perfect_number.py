def perfect_number(number):
    is_perfect = True
    output = 0
    for current_num in range(1, number):
        if number % current_num == 0:
            output += current_num
    if output != number:
        is_perfect = False
        print("It's not so perfect.")
    return is_perfect


digit = int(input())
number_is_perfect = perfect_number(digit)
if number_is_perfect:
    print('We have a perfect number!')