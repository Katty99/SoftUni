budget = float(input())
statists = int(input())
price_clothing_per_statist = float(input())
decor_cost = budget * 0.1
clothing_cost = statists * price_clothing_per_statist

if statists > 150:
    cost = decor_cost + clothing_cost - (clothing_cost * 0.1)

else:
    cost = decor_cost + clothing_cost

if cost > budget:
    print(f' Not enough money!')
    deficit = cost - budget
    print(f'Wingard needs{deficit: .2f} leva more.')
else:
    print(f'Action!')
    left_amount = budget - cost
    print(f'Wingard starts filming with{left_amount: .2f} leva left.')
