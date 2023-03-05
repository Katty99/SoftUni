import sys

number = int(input())
max_number = - sys.maxsize
total_number = 0
sum_smaller_numbers = 0
for _ in range(number):
    current_number = int(input())
    total_number += current_number
    if current_number > max_number:
        max_number = current_number
sum_smaller_numbers = total_number - max_number
if sum_smaller_numbers == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference = abs(sum_smaller_numbers - max_number)
    print('No')
    print(f'Diff = {difference}')
