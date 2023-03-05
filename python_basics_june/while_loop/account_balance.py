total = 0
while True:

    command = (input())
    if command == 'NoMoreMoney':
        break

    installment = float(command)

    if installment >= 0:
        total += installment
        print(f'Increase:{installment: .2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total:{total: .2f}')
