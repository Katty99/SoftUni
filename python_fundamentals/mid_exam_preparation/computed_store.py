total_no_tax = 0
total_cost = 0
taxes = 0

while True:
    command = input()
    if command == 'special':
        taxes += total_cost * 0.2
        total_cost += taxes
        total_cost -= total_cost * 0.1
        break
    if command == 'regular':
        taxes += total_cost * 0.2
        total_cost += taxes
        break
    if float(command) <= 0:
        print('Invalid price!')
        continue
    else:
        total_no_tax += float(command)
        total_cost += float(command)

if total_no_tax > 0:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_no_tax:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_cost:.2f}$')
else:
    print('Invalid order!')
