import re

line = input()
furniture = []
total_money = 0
pattern = r'>>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)'

while line != 'Purchase':
    matches = re.search(pattern, line)
    if matches:
        piece, price, quantity = matches.groups()
        furniture.append(piece)
        total_money += float(price) * int(quantity)
    line = input()
print("Bought furniture:")
if furniture:
    for current in furniture:
        print(current)
print(f"Total money spend: {total_money:.2f}")
