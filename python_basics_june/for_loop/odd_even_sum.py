n = int(input())
sum_even_numbers = 0
sum_odd_numbers = 0
for i in range(1, n + 1):
    current_number = int(input())
    if i % 2 == 0:
        sum_even_numbers += current_number
    else:
        sum_odd_numbers += current_number
if sum_even_numbers == sum_odd_numbers:
    print(f'Yes')
    print(f'Sum = {sum_odd_numbers}')
else:
    diff = abs(sum_odd_numbers - sum_even_numbers)
    print(f'No')
    print(f'Diff = {diff}')
