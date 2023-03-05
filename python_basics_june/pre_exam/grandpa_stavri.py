number_of_days = int(input())
liters_counter = 0
degrees_counter = 0
for current_day in range(1, number_of_days + 1):
    quantity = float(input())
    degree = float(input())
    total_degrees = degree * quantity
    liters_counter += quantity
    degrees_counter += total_degrees
average_degrees = degrees_counter / liters_counter
print(f'Liter: {liters_counter:.2f}')
print(f'Degrees: {average_degrees:.2f}')
if average_degrees < 38:
    print(f'Not good, you should baking!')
elif average_degrees <= 42:
    print(f'Super!')
else:
    print(f'Dilution with distilled water!')
