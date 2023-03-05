number_of_people = int(input())
season = input()
if season == 'spring':
    if number_of_people <= 5:
        cost = number_of_people * 50
    else:
        cost = number_of_people * 48
elif season == 'summer':
    if number_of_people <= 5:
        cost = number_of_people * 48.5
    else:
        cost = number_of_people * 45
elif season == 'autumn':
    if number_of_people <= 5:
        cost = number_of_people * 60
    else:
        cost = number_of_people * 49.5
else:
    if number_of_people <= 5:
        cost = number_of_people * 86
    else:
        cost = number_of_people * 85
if season == 'summer':
    cost -= cost * 15 / 100
elif season == 'winter':
    cost += cost * 8 / 100
print(f'{cost:.2f} leva.')

