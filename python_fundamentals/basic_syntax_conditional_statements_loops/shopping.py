budget = int(input())
command = input()
while command != 'End':
    spent = int(command)
    budget -= spent
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
if budget >= 0:
    print('You bought everything needed.')
