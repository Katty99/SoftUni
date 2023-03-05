items_and_prices = input().split('|')
budget = float(input())
valid_list = []
profit = 0
new_prices = 0
for current_item_price in items_and_prices:
    separated = current_item_price.split('->')
    item_type = separated[0]
    price = float(separated[1])
    is_valid = False
    if price > budget:
        continue
    if item_type == 'Clothes':
        if price <= 50:
            is_valid = True
        else:
            continue
    elif item_type == 'Shoes':
        if price <= 35:
            is_valid = True
        else:
            continue
    elif item_type == 'Accessories':
        if price <= 20.5:
            is_valid = True
        else:
            continue
    if is_valid:
        budget -= price
        profit += price * 0.4
        selling_price = price + price * 0.40
        new_prices += selling_price
        valid_list.append('%.2f' % selling_price)

print(*valid_list, sep=' ')
print(f'Profit: {profit:.2f}')
if budget + new_prices >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
