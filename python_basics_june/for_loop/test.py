n = int(input())
even_number_sum = 0
odd_number_sum = 0

for i in range(1, n+1):
    current_number = int(input())
    if i % 2 == 0:
        even_number_sum += current_number
    else:
        odd_number_sum += current_number
if even_number_sum == odd_number_sum:
    print(f'Yes')
    print(f'Sum = {even_number_sum}')
else:
    diff = abs(even_number_sum - odd_number_sum)
    print(f'No')
    print(f'Diff = {diff}')



