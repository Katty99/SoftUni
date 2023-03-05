food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
weight = float(input()) * 1000
no_food = False
for current_day in range(1, 31):
    food_quantity -= 300
    if current_day % 2 == 0:
        hay_quantity -= food_quantity * 0.05
    if current_day % 3 == 0:
        cover_quantity -= weight * 1 / 3
    if food_quantity < 0 or hay_quantity < 0 or cover_quantity < 0:
        no_food = True
        print('Merry must go to the pet store!')
        break
if not no_food:
    print(f'Everything is fine! Puppy is happy! Food: {food_quantity / 1000:.2f}, Hay: {hay_quantity / 1000:.2f}\
, Cover: {cover_quantity / 1000:.2f}.')