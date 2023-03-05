budget = int(input())
season = input()
number_of_fishers = int(input())
price = 0
additional_discount = 0

if season == 'Spring':
    price = 3000
    if number_of_fishers <= 6:
        price = price - price * 0.1
    elif number_of_fishers <= 11:
        price = price - price * 0.15
    else:
        price = price - price * 0.25
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if number_of_fishers <= 6:
        price = price - price * 0.1
    elif number_of_fishers <= 11:
        price = price - price * 0.15
    else:
        price = price - price * 0.25
else:
    price = 2600
    if number_of_fishers <= 6:
        price = price - price * 0.1
    elif number_of_fishers <= 11:
        price = price - price * 0.15
    else:
        price = price - price * 0.25
if number_of_fishers % 2 == 0 and season != 'Autumn':
    price = price - price * 0.05

difference = abs(price - budget)
if price <= budget:
    print(f'Yes! You have{difference: .2f} leva left.')
else:
    print(f'Not enough money! You need{difference: .2f} leva.')


