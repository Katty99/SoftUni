budget = float(input())
flour_kg_price = float(input())
colored_eggs_counter = 0
current_bread_counter = 0
eggs_price = flour_kg_price * 0.75
milk_price = (flour_kg_price + flour_kg_price * 0.25) / 4
cost_per_bread = flour_kg_price + eggs_price + milk_price
while budget > cost_per_bread:
    budget -= cost_per_bread
    current_bread_counter += 1
    colored_eggs_counter += 3
    if current_bread_counter % 3 == 0:
        colored_eggs_counter -= current_bread_counter - 2
print(f'You made {current_bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and \
{budget:.2f}BGN left.')
