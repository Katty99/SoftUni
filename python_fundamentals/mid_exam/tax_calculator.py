vehicles = input().split('>>')
total_taxes = 0
for current_vehicle in range(len(vehicles)):
    components = vehicles[current_vehicle].split()
    car_type = components[0]
    years = int(components[1])
    kilometers = int(components[2])
    if car_type == 'family':
        tax_increase = kilometers // 3000 * 12
        tax_decrease = years * 5
        tax = tax_increase + (50 - tax_decrease)
        total_taxes += tax
    elif car_type == 'heavyDuty':
        tax_decrease = years * 8
        tax_increase = kilometers // 9000 * 14
        tax = tax_increase + (80 - tax_decrease)
        total_taxes += tax
    elif car_type == 'sports':
        tax_decrease = years * 9
        tax_increase = kilometers // 2000 * 18
        tax = tax_increase + (100 - tax_decrease)
        total_taxes += tax
    else:
        print("Invalid car type.")
        continue
    print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")