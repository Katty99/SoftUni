flower_kind = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if flower_kind == 'Roses':
    price = 5
    if number_of_flowers > 80:
        price = price - price * 0.1
elif flower_kind == 'Dahlias':
    price = 3.8
    if number_of_flowers > 90:
        price = price - price * 0.15
elif flower_kind == 'Tulips':
    price = 2.8
    if number_of_flowers > 80:
        price = price - price * 0.15
elif flower_kind == 'Narcissus':
    price = 3
    if number_of_flowers < 120:
        price = price + price * 0.15
elif flower_kind == 'Gladiolus':
    price = 2.5
    if number_of_flowers < 80:
        price = price + price * 0.2
total_sum = price * number_of_flowers
difference = abs(total_sum - budget)

if budget >= total_sum:
    print(f'Hey, you have a great garden with {number_of_flowers} {flower_kind} and{difference: .2f} leva left.')
else:
    print(f'Not enough money, you need{difference: .2f} leva more.')
