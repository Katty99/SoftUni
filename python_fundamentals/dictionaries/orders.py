final = {}
prices = {}
while True:
    command = input()
    if command == 'buy':
        break
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in final.keys():
        final[product] = 0
        prices[product] = 0.00
    final[product] += quantity
    prices[product] = price
for key, value in final.items():
    value *= prices[key]
    print(f"{key} -> {value:.2f}")

