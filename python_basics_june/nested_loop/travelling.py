destination = input()
while destination != 'End':
    minimum_budget = float(input())
    saved_amount = 0
    while saved_amount < minimum_budget:
        amount = float(input())
        saved_amount += amount
        if saved_amount >= minimum_budget:
            print(f'Going to {destination}!')
    destination = input()
