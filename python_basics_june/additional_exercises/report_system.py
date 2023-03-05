sum_expected = int(input())
transactions_count = 0
current_sum = 0
number_of_card_payments = 0
number_of_cash_payments = 0
sum_paid_with_card = 0
sum_paid_in_cash = 0
while current_sum < sum_expected:
    command = input()
    if command != 'End':
        amount = int(command)
        transactions_count += 1
        if transactions_count % 2 == 0:
            if amount < 10:
                print(f'Error in transaction!')
            else:
                sum_paid_with_card += amount
                current_sum += amount
                number_of_card_payments += 1
                print(f'Product sold!')
        else:
            if amount > 100:
                print(f'Error in transaction!')
            else:
                current_sum += amount
                sum_paid_in_cash += amount
                number_of_cash_payments += 1
                print(f'Product sold!')
    else:
        break

if number_of_card_payments != 0:
    average_card = sum_paid_with_card / number_of_card_payments
else:
    average_card = 0
if number_of_cash_payments != 0:
    average_cash = sum_paid_in_cash / number_of_cash_payments
else:
    average_cash = 0

if current_sum >= sum_expected:
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')
else:
    print(f'Failed to collect required money for charity.')
