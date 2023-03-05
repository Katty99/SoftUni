budget = float(input())
season = input()
price = 0
destination = ''
accommodation = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        price = budget * 0.3
    elif season == 'winter':
        price = budget * 0.7
        accommodation = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        price = budget * 0.4
    elif season == 'winter':
        accommodation = 'Hotel'
        price = budget * 0.8
else:
    destination = 'Europe'
    price = budget * 0.9
    accommodation = 'Hotel'
print(f'Somewhere in {destination}')
print(f'{accommodation} -{price: .2f}')
