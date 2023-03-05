from math import ceil
name = input()
budget_available = float(input())
number_of_beers = int(input())
number_of_chips_packs = int(input())
beer_cost = number_of_beers * 1.2
chips_cost = ceil(number_of_chips_packs * (beer_cost * 45 / 100))
total_cost = beer_cost + chips_cost
difference = abs(budget_available - total_cost)
if budget_available >= total_cost:
    print(f'{name} bought a snack and has {difference:.2f} leva left.')
else:
    print(f'{name} needs {difference:.2f} more leva!')