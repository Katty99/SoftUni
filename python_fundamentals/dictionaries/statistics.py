total_quantity = 0
products = {}
while True:
    command = input()
    if command == 'statistics':
        break
    key, value = command.split(': ')
    if key not in products.keys():
        products[key] = 0
    products[key] += int(value)
    total_quantity += int(value)

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {total_quantity}")

