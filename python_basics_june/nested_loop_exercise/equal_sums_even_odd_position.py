min_number = int(input())
max_number = int(input())

for number in range(min_number, max_number + 1):
    even_number = 0
    odd_number = 0
    num_to_str = str(number)
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            odd_number += int(digit)
        else:
            even_number += int(digit)
    if odd_number == even_number:
        print(num_to_str, end=' ')

