screening_type = input()
rows = int(input())
columns = int(input())
price = 0

if screening_type == 'Premiere':
    price = 12
elif screening_type == 'Normal':
    price = 7.5
elif screening_type == 'Discount':
    price = 5

total_sum = rows * columns * price
print(f'{total_sum: .2f} leva')
