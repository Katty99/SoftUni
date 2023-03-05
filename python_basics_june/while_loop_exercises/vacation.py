money_needed = float(input())
money_available = float(input())
days_spending = 0
days_passed = 0
spending_too_many_days = False
while money_available < money_needed:
    action = input()
    amount = float(input())
    days_passed += 1
    if action == 'spend':
        days_spending += 1
        if days_spending == 5:
            spending_too_many_days = True
            break
        money_available -= amount
        if money_available < 0:
            money_available = 0
    else:
        money_available += amount
        days_spending = 0
if spending_too_many_days:
    print(f"You can't save the money.")
    print(f'{days_passed}')
else:
    print(f'You saved the money for {days_passed} days.')
