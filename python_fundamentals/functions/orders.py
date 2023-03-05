def total(quantity):
    if order == 'coffee':
        return quantity * 1.5
    elif order == 'water':
        return quantity * 1
    elif order == 'coke':
        return quantity * 1.4
    elif order == 'snacks':
        return quantity * 2


order = input()
quantity = int(input())
print(f'{total(quantity):.2f}')