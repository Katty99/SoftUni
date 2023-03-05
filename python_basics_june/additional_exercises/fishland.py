mackerel_price = float(input())
sprat_price = float(input())
bonito_quantity = float(input())
scad_quantity = float(input())
mussels_quantity = float(input())
bonito_price = mackerel_price + mackerel_price * 0.6
scad_price = sprat_price + sprat_price * 0.8
mussels_price = 7.5
total = bonito_quantity * bonito_price + scad_quantity * scad_price + mussels_quantity * mussels_price
print(f'{total: .2f}')
