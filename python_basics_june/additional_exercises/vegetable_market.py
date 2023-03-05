vegetables_price = float(input())
fruits_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
total_revenue_lv = (vegetables_kg * vegetables_price) + (fruits_price * fruits_kg)
total_revenue_eur = total_revenue_lv / 1.94
print(f'{total_revenue_eur: .2f}')
