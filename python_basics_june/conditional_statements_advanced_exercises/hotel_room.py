month = input()
stay_duration = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if stay_duration > 14:
        apartment_price *= 0.9
        studio_price *= 0.7
    elif 7 < stay_duration <= 14:
        studio_price *= 0.95
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if stay_duration > 14:
        apartment_price *= 0.9
        studio_price *= 0.8
else:
    studio_price = 76
    apartment_price = 77
    if stay_duration > 14:
        apartment_price *= 0.9

apartment_cost = apartment_price * stay_duration
studio_cost = studio_price * stay_duration
print(f'Apartment:{apartment_cost: .2f} lv.')
print(f'Studio:{studio_cost: .2f} lv.')
